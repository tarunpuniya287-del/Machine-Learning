import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fluid Simulation with Shake Control")

# Colors
BG_COLOR = (20, 20, 30)
PARTICLE_COLOR = (100, 200, 250)

# Fluid particles
particles = []
num_particles = 200

# Particle properties
radius = 5
gravity = 0.3
bounce = -0.7

# Create particles
for _ in range(num_particles):
    x = random.randint(150, 350)
    y = random.randint(300, 650)
    particles.append([x, y, 0, 0])  # [x, y, vx, vy]

# Bottle boundaries
left_wall = 150
right_wall = 350
top_wall = 250
bottom_wall = 650

clock = pygame.time.Clock()
running = True

# Shake force values
shake_force = 0

while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls for shaking the bottle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shake_force = -3  # Shake left
            if event.key == pygame.K_RIGHT:
                shake_force = 3   # Shake right

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                shake_force = 0  # Stop shaking

    # Simulate particle motion
    for p in particles:
        x, y, vx, vy = p

        # Apply gravity
        vy += gravity

        # Apply shake force
        vx += shake_force * 0.1

        # Update position
        x += vx
        y += vy

        # Collide with walls
        if x - radius < left_wall:
            x = left_wall + radius
            vx *= bounce
        if x + radius > right_wall:
            x = right_wall - radius
            vx *= bounce
        if y - radius < top_wall:
            y = top_wall + radius
            vy *= bounce
        if y + radius > bottom_wall:
            y = bottom_wall - radius
            vy *= bounce

        # Friction to gradually slow down particles horizontally
        vx *= 0.98

        # Update particle values
        p[0], p[1], p[2], p[3] = x, y, vx, vy

        # Draw particle
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(x), int(y)), radius)

    # Draw bottle outline
    pygame.draw.rect(screen, (200, 200, 200), (left_wall, top_wall, right_wall - left_wall, bottom_wall - top_wall), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
