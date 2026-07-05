import pygame
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('match the following')
running=True
ninja=pygame.image.load('ninja-removebg-preview.png')
ninja=pygame.transform.scale(ninja,(100,100))
archer=pygame.image.load('archer_-removebg-preview.png')
archer=pygame.transform.scale(archer,(100,100))
wizard=pygame.image.load('The_Wizard-removebg-preview.png')
wizard=pygame.transform.scale(wizard,(100,100))
ninjasprite=ninja.get_rect()
archersprite=archer.get_rect()
wizardsprite=wizard.get_rect()
ninjasprite.center=(100,100)
archersprite.center=(400,100)
wizardsprite.center=(700,100)

sword=pygame.image.load('sword-removebg-preview.png')
sword=pygame.transform.scale(sword,(100,100))
swordsprite=sword.get_rect()
swordsprite.center=(100,600)
bow=pygame.image.load('bow-removebg-preview.png')
bow=pygame.transform.scale(bow,(100,100))
bowsprite=bow.get_rect()
bowsprite.center=(400,600)
staff=pygame.image.load('stafff-removebg-preview.png')
staff=pygame.transform.scale(staff,(100,100))
staffsprite=staff.get_rect()
staffsprite.center=(700,600)
font1=pygame.font.SysFont('Arial',25)
text1=font1.render('match the following',True,"black")


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 
    screen.fill('blue')

    screen.blit(ninja,ninjasprite)
    screen.blit(archer,archersprite)
    screen.blit(wizard,wizardsprite)
    screen.blit(sword,swordsprite)
    screen.blit(bow,bowsprite)
    screen.blit(staff,staffsprite)
    screen.blit(text1,(300,700))
    pygame.display.update()
pygame.quit()