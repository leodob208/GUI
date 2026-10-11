import  pygame
import random
screen = pygame.display.set_mode((800, 600))
width = 800
height = 600
white = (255, 255, 255)
blue = (0, 0, 255)
ship = pygame.image.load("rocket-removebg-preview.png")
bug = pygame.image.load("snail-removebg-preview.png")
ship.pos = ship.get_rect(center=(width / 2, height - 50))
speed = 5
bullets = []
enimes = []
for x in range(8):
    enimes.append(bug.get_rect(center=(random.randint(0, width), random.randint(-150, -50))))
    enimes[1].y =80
    enimes[2].x = 100+ 90*x


def displayscrore(score):
   screen.draw.text(str(score,(50,50)))


def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(ship.pos.midtop)
        bullets[-1].y = ship.pos.y - 10
        bullets[-1].x = ship.pos.x

def update():
    global score
    if keyboard.left:
        ship.pos.x -= speed
    if keyboard.right:
        ship.pos.x += speed
    for bullet in bullets:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)
    for enemy in enimes:
        enemy.y += 2
        if enemy.y > height:
            enemy.y = random.randint(-150, -50)
            enemy.x = random.randint(0, width)
