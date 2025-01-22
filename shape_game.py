import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game variables
shapes = ['circle', 'square', 'triangle']
current_shape = random.choice(shapes)

# Function to draw shapes
def draw_shape(shape, x, y):
    if shape == 'circle':
        pygame.draw.circle(screen, RED, (x, y), 40)
    elif shape == 'square':
        pygame.draw.rect(screen, GREEN, (x-40, y-40, 80, 80))
    elif shape == 'triangle':
        pygame.draw.polygon(screen, BLUE, [(x, y-40), (x-40, y+40), (x+40, y+40)])

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Display instruction
    font = pygame.font.Font(None, 36)
    text = font.render(f"Click the {current_shape}", True, BLACK)
    screen.blit(text, (WIDTH//2 - 100, 20))
    
    # Draw shapes at random positions
    positions = [(150, 200), (300, 200), (450, 200)]
    random.shuffle(positions)
    shape_dict = {}
    
    for i, shape in enumerate(shapes):
        x, y = positions[i]
        draw_shape(shape, x, y)
        shape_dict[(x, y)] = shape
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            for (x, y), shape in shape_dict.items():
                if shape == 'circle' and ((mx - x)**2 + (my - y)**2) <= 1600:
                    if shape == current_shape:
                        current_shape = random.choice(shapes)
                elif shape == 'square' and (x-40 <= mx <= x+40 and y-40 <= my <= y+40):
                    if shape == current_shape:
                        current_shape = random.choice(shapes)
                elif shape == 'triangle' and (y - 40 <= my <= y + 40 and x - 40 <= mx <= x + 40):
                    if shape == current_shape:
                        current_shape = random.choice(shapes)

pygame.quit()
