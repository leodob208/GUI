from email.mime import image

import pygame 
pygame.init ()
screen=pygame .display.set_mode((800,800))
pygame.display.set_caption ('key events ')
running=True
image1=pygame.image.load('rocket.jpeg')
image1=pygame.transform.scale(image1,(100,100))
rocket=image1.get_rect()
rocket.center=(200,200)
image2=pygame.image.load('ufo.jpeg')
image2=pygame.transform.scale(image2,(100,100))
ufo=image2.get_rect()
ufo.center=(600,600)
image3=pygame.image.load('71dNtlbI7fL.jpg')
image3=pygame.transform.scale(image3,(800,800))

while running:
    for event in pygame .event.get ():
        if event.type==pygame.QUIT :
             running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: 
        rocket.x-=5
    if keys[pygame.K_RIGHT]:
        rocket.x+=5
    if keys[pygame.K_UP]:
        rocket.y-=5
    if keys[pygame.K_DOWN]:
        rocket.y+=5
    screen.blit (image3,(0,0))
    screen.blit(image1,rocket)
    screen.blit(image2,ufo)
   
    pygame.display.update()
pygame.quit()