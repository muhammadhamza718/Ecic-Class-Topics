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

# Create an alpha surface for trail effect
trail_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
trail_surface.fill((10, 10, 15, 60))

angle_offset = 0
radius = 320
speed = 0.4

running = True
while running:
    clock.tick(60)
    time_ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Trail effect overlay instead of full clear
    screen.blit(trail_surface, (0, 0))

    cx = WIDTH // 2
    cy = HEIGHT // 2

    # Draw center text with a pulsing color and subtle vertical bounce effect
    pulse = (math.sin(time_ticks * 0.003) + 1) / 2 # 0.0 to 1.0
    val_r = int(150 + 105 * pulse)
    val_g = int(200 + 55 * pulse)
    val_b = 255
    center_y_offset = math.sin(time_ticks * 0.005) * 10
    
    center_surface = center_font.render(center_text, True, (val_r, val_g, val_b))
    
    # A subtle shadow for the center text
    shadow_surface = center_font.render(center_text, True, (0, 0, 50))
    center_rect = center_surface.get_rect(center=(cx, cy + center_y_offset))
    shadow_rect = shadow_surface.get_rect(center=(cx + 4, cy + center_y_offset + 4))
    
    screen.blit(shadow_surface, shadow_rect)
    screen.blit(center_surface, center_rect)

    total_words = len(words)

    for i, word in enumerate(words):
        theta = math.radians(angle_offset) + (2 * math.pi * i / total_words)

        x = cx + radius * math.cos(theta)
        y = cy + radius * math.sin(theta)

        # Calculate a dynamic rainbow color shifting over time and position
        hue = (i * (360 / total_words) + time_ticks * 0.05) % 360
        color = pygame.Color(0)
        color.hsva = (hue, 80, 100, 100)

        # Dynamic scaling based on vertical position (gives a 3D effect illusion)
        # Closer (bottom: positive y offset) appears larger, further (top: negative) appears smaller
        scale_factor = 0.8 + (math.sin(theta) * 0.3)
        
        # Render the text dynamically each frame to apply the shifting color
        word_surf = circle_font.render(word, True, color)
        
        # Scale for 3D depth illusion
        if abs(scale_factor - 1.0) > 0.01:
            word_surf = pygame.transform.rotozoom(word_surf, 0, scale_factor)

        rect = word_surf.get_rect(center=(x, y))
        screen.blit(word_surf, rect)

    angle_offset += speed

    pygame.display.flip()

pygame.quit()
sys.exit()