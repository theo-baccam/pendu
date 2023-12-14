import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
width = pygame.Vector2(screen.get_width())
height = pygame.Vector2(screen.get_height())
print(width)
print(height)
clock = pygame.time.Clock()
running = True

background = [255, 255, 255]
i = 100
while running:
    screen.fill((background))
    keys = pygame.key.get_pressed()
    pygame.draw.circle(screen, "blue", width / 2, height / 2, i)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_UP]:
            i += 5
        if keys[pygame.K_DOWN]:
            i -= 5
    pygame.display.flip()

pygame.quit()