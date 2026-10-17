import random
from pathlib import Path

import pygame


WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
LASER_GLOW = (0, 150, 255)
LASER_COLOR = (90, 235, 255)
LASER_CORE = (255, 255, 255)
BLACK = (0, 0, 0)
SHIP_SPEED = 5
LASER_SPEED = 12
ENEMY_SPEED = 2
ENEMY_COUNT = 4


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Galaga")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    asset_dir = Path(__file__).resolve().parent
    ship_image = pygame.image.load(asset_dir / "rocket-removebg-preview.png").convert_alpha()
    enemy_image = pygame.image.load(asset_dir / "snail-removebg-preview.png").convert_alpha()
    enemy_image = pygame.transform.smoothscale(
        enemy_image,
        (max(1, enemy_image.get_width() // 4), max(1, enemy_image.get_height() // 4)),
    )
    ship = ship_image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 20))
    enemies = [
        enemy_image.get_rect(
            midtop=(WIDTH * (index + 1) // (ENEMY_COUNT + 1), random.randint(-180, -40))
        )
        for index in range(ENEMY_COUNT)
    ]
    bullets = []
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(ship.centerx - 4, ship.top - 24, 8, 24))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ship.x -= SHIP_SPEED
        if keys[pygame.K_RIGHT]:
            ship.x += SHIP_SPEED
        ship.clamp_ip(screen.get_rect())

        for enemy in enemies:
            enemy.y += ENEMY_SPEED
            if enemy.top > HEIGHT:
                enemy.midtop = (
                    random.randint(enemy.width // 2, WIDTH - enemy.width // 2),
                    random.randint(-180, -40),
                )

        remaining_bullets = []
        for bullet in bullets:
            bullet.y -= LASER_SPEED
            hit_enemy = next((enemy for enemy in enemies if bullet.colliderect(enemy)), None)
            if hit_enemy is not None:
                score += 1
                hit_enemy.midtop = (
                    random.randint(hit_enemy.width // 2, WIDTH - hit_enemy.width // 2),
                    random.randint(-180, -40),
                )
            elif bullet.bottom >= 0:
                remaining_bullets.append(bullet)
        bullets = remaining_bullets

        screen.fill(BLACK)
        screen.blit(ship_image, ship)
        for enemy in enemies:
            screen.blit(enemy_image, enemy)
        for bullet in bullets:
            pygame.draw.rect(screen, LASER_GLOW, bullet.inflate(8, 6), border_radius=6)
            pygame.draw.rect(screen, LASER_COLOR, bullet, border_radius=4)
            core = bullet.inflate(-4, -2)
            pygame.draw.rect(screen, LASER_CORE, core, border_radius=2)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (12, 12))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
