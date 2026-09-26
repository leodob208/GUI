import pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("car racing game")
#pratice work create a screen for car racing game and add the sprite of car on the bottom og the screen  and road and make the car move up and down and left and right using arrow keys
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Car Racing Game")
clock = pygame.time.Clock()
obstcal2_image = pygame.image.load("acone-removebg-preview.png").convert_alpha()
obstcal2_image = pygame.transform.scale(obstcal2_image, (60, 100))
obstaclsprite2 = obstcal2_image.get_rect(midbottom=(400, 0))
obstaclsprite2.center=(400,0)
highway = pygame.image.load("highway .jpg").convert()
highway = pygame.transform.scale(highway, (800, 800))
highway = pygame.transform.rotate(highway, 90)
highway2= pygame.image.load("highway .jpg").convert()
highway2 = pygame.transform.scale(highway2, (800, 800))
highway2 = pygame.transform.rotate(highway2, 90)
car_image = pygame.image.load("race_carr-removebg-preview.png").convert_alpha()
car_image = pygame.transform.scale(car_image, (60, 100))
obstacle= pygame.image.load("cone-removebg-preview.png").convert_alpha()
obstacle = pygame.transform.scale(obstacle, (60, 60))
obstaclesprite=obstacle.get_rect()



car = car_image.get_rect(midbottom=(400, 770))
speed = 5
running = True
hy1 = 0
hy2 = -800
while running:
    hy1 += 5
    hy2 += 5

    if hy1 >=800:
        hy1 = -800
    if hy2 >=800:
        hy2 = -800

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car.x -= speed
    if keys[pygame.K_RIGHT]:
        car.x += speed
    if keys[pygame.K_UP]:
        car.y -= speed
    if keys[pygame.K_DOWN]:
        car.y += speed

    

    screen.blit(highway, (0, hy1))
    screen.blit(highway2, (0, hy2))
    screen.blit(car_image, car)
    screen.blit(obstcal2_image, obstaclsprite2)
    screen.blit(obstacle, obstaclesprite)
    pygame.display.update()
    

pygame.quit()