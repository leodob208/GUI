import pygame 
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('flappy bird game ')
gameloop=True
bgimage=pygame.image.load('flappy brid sky .jpeg')
bgimage=pygame.transform.scale(bgimage,(800,800))
bird=pygame.image.load('flappy_brid_-removebg-preview 2.png')
bird=pygame.transform.scale(bird,(100,100))
birdsprite=bird.get_rect()
birdsprite.center=(100,400)
pipe=pygame.image.load('new_pipes_-removebg-preview.png')
pipe=pygame.transform.scale(pipe,(650,800))
pipesprite1=pipe.get_rect()
pipesprite1.center=(450,400)
pipesprite2=pipe.get_rect()
pipesprite2.center=(900,400)
vx= 0.51
while gameloop:
    pipesprite1.x=pipesprite1.x-vx
    pipesprite2.x=pipesprite2.x-vx
    for event in pygame .event.get ():
        if event.type==pygame.QUIT :
             gameloop=False
    screen.fill('blue')
    screen.blit(bgimage, (0,0))
    screen.blit(bird, birdsprite)
    screen.blit(pipe, pipesprite1)
    screen.blit(pipe, pipesprite2)
    pygame.display.update()
    if pipesprite1.x<20:
      pipesprite1.x=900
    if pipesprite2.x<20:
      pipesprite2.x=900
pygame.quit()  
     