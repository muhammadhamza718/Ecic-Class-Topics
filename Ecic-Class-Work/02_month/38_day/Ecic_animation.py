import pygame
import math
import sys

pygame.init()

WIDTH = 1000
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Word Circle")

clock = pygame.time.Clock()

center_text = "BBSHRRDB"
circle_text = "BENAZIR BHUTTO SHAHEED HUMAN RESOURCE RESEARCH & DEVELOPMENT BOARD"

# Split into words
words = circle_text.split()

center_font = pygame.font.SysFont("arial", 90, bold=True)
circle_font = pygame.font.SysFont("arial", 28, bold=True)

# Pre-render word surfaces
word_surfaces = []
for word in words:
    surface = circle_font.render(word, True, (150, 200, 255))
    word_surfaces.append(surface)

angle_offset = 0
radius = 280
speed = 0.4

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 10, 15))

    cx = WIDTH // 2
    cy = HEIGHT // 2

    # Draw center text
    center_surface = center_font.render(center_text, True, (220, 220, 220))
    center_rect = center_surface.get_rect(center=(cx, cy))
    screen.blit(center_surface, center_rect)

    total_words = len(word_surfaces)

    for i, surface in enumerate(word_surfaces):
        theta = math.radians(angle_offset) + (2 * math.pi * i / total_words)

        x = cx + radius * math.cos(theta)
        y = cy + radius * math.sin(theta)

        rect = surface.get_rect(center=(x, y))
        screen.blit(surface, rect)

    angle_offset += speed

    pygame.display.flip()

pygame.quit()
sys.exit()