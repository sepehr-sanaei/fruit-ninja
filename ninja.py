import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load fruit images
FRUIT_IMAGES = []
for img_name in ['apple.png', 'banana.png', 'orange.png']:
    img = pygame.image.load(os.path.join('images', img_name))
    FRUIT_IMAGES.append(pygame.transform.scale(img, (50, 50)))

# Font for score and messages
FONT = pygame.font.Font(None, 36)
LARGE_FONT = pygame.font.Font(None, 72)

# Fruit class
class Fruit:
    def __init__(self):
        self.image = random.choice(FRUIT_IMAGES)
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH-50), HEIGHT + 50))
        self.speed = random.randint(3, 10)
    
    def move(self):
        self.rect.y -= self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Main game function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Fruit Ninja Simplified')
    
    clock = pygame.time.Clock()
    fruits = []
    score = 0
    missed_fruits = 0
    running = True
    game_over = False
    
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                pos = pygame.mouse.get_pos()
                for fruit in fruits:
                    if fruit.rect.collidepoint(pos):
                        fruits.remove(fruit)
                        score += 1
        
        if not game_over:
            if random.randint(1, 20) == 1:
                fruits.append(Fruit())
            
            for fruit in fruits:
                fruit.move()
                fruit.draw(screen)
                if fruit.rect.bottom < 0:
                    fruits.remove(fruit)
                    missed_fruits += 1
                    if missed_fruits >= 10:
                        game_over = True
        
        score_text = FONT.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        missed_text = FONT.render(f"Missed: {missed_fruits}", True, BLACK)
        screen.blit(missed_text, (10, 50))
        
        if game_over:
            lose_text = LARGE_FONT.render("You Lose", True, RED)
            screen.blit(lose_text, (WIDTH // 2 - lose_text.get_width() // 2, HEIGHT // 2 - lose_text.get_height() // 2))
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()
