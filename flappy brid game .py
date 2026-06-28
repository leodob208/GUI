import pygame 
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('flappy bird game ')
gameloop=True
bgimage=pygame.image.load('flappy brid sky .jpeg')
bgimage=pygame.transform.scale(bgimage,(800,800))
bird=pygame.image.load('flappy_brid_-removebg-preview 2.png')
bird=pygame.transform.scale(bird,(65,65))
birdsprite=bird.get_rect()
by=400
birdsprite.center=(440,by)
pipe=pygame.image.load('bottom of pipe .png')
pipe=pygame.transform.scale(pipe,(150,350))
pipesprite1=pipe.get_rect()
pipesprite1.center=(330,550)
pipesprite2=pipe.get_rect()
gameover=pygame.mixer_music.load('GAMEOVER.mp3')
pipesprite2.center=(1050,550)
pipetop=pygame.image.load('top pipe.png')
pipetop=pygame.transform.scale(pipetop,(150,220))
pipetopsprite1=pipetop.get_rect()
pipetopsprite1.center=(330,0)
pipetopsprite2=pipetop.get_rect()
pipetopsprite2.center=(1050,0)

vx= 0.51
gravity=0.5
font1=pygame.font.SysFont('Arial', 25)
score=0
text1=font1.render('score: '+str(score),True,'black')
while gameloop:
    pipesprite1.x=pipesprite1.x-vx
    pipesprite2.x=pipesprite2.x-vx
    pipetopsprite1.x=pipetopsprite1.x-vx
    pipetopsprite2.x=pipetopsprite2.x-vx
    by+=gravity
    for event in pygame .event.get ():
        if event.type==pygame.QUIT :
             gameloop=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        by-=3
    screen.fill('blue')
    screen.blit(bgimage, (0,0))
    screen.blit(bird, birdsprite)
    screen.blit(pipe, pipesprite1)
    screen.blit(pipe, pipesprite2)
    screen.blit(pipetop, pipetopsprite1)
    screen.blit(pipetop, pipetopsprite2)
    screen.blit(text1,(400,700))
    birdsprite.center=(440,by)
    pygame.display.update()
    if pipesprite1.x<20:
      pipesprite1.x=1050
    if pipesprite2.x<20:
      pipesprite2.x=1050
      score+=1
      text1=font1.render('score: '+str(score),True,'black')
    if pipetopsprite1.x<20:
      pipetopsprite1.x=1050
    if pipetopsprite2.x<20:
      pipetopsprite2.x=1050
      score+=1
    if pipesprite1.colliderect(birdsprite):
      print('skill issue')
      vx=0
      by=0
      gravity=0
      pygame.mixer_music.play()
      
    if pipesprite2.colliderect(birdsprite):
      vx=0
      by=0
      gravity=0
      pygame.mixer_music.play()
      print('skill issue')
      

pygame.quit()  
     