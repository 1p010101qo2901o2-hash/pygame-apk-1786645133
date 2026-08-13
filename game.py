

import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 450

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "My Pygame Android Game"
)

clock = pygame.time.Clock()

font = pygame.font.Font(
    None,
    48
)

player = pygame.Rect(
    100,
    200,
    50,
    50
)

enemy = pygame.Rect(
    700,
    random.randint(50, 400),
    40,
    40
)

score = 0

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False


    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        player.x -= 6

    if keys[pygame.K_RIGHT]:
        player.x += 6

    if keys[pygame.K_UP]:
        player.y -= 6

    if keys[pygame.K_DOWN]:
        player.y += 6


    player.clamp_ip(
        screen.get_rect()
    )


    enemy.x -= 5


    if enemy.right < 0:

        enemy.x = WIDTH + 50

        enemy.y = random.randint(
            50,
            HEIGHT - 50
        )

        score += 1


    if player.colliderect(enemy):

        score = 0

        enemy.x = WIDTH + 50


    screen.fill(
        (7, 10, 28)
    )


    pygame.draw.rect(
        screen,
        (0, 220, 255),
        player,
        border_radius=12
    )


    pygame.draw.rect(
        screen,
        (255, 50, 110),
        enemy,
        border_radius=12
    )


    text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255)
    )

    screen.blit(
        text,
        (20, 20)
    )


    pygame.display.flip()

    clock.tick(60)


pygame.quit()

sys.exit()
