import pygame 
pygame.init()
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption('recycling game ')
gameloop=True
greenbin=pygame.image.load('the only green bin .jpeg')
redbin=pygame.image.load('only the red bin .jpeg')
greenbin=pygame.transform.scale(greenbin,(100,100))
redbin=pygame.transform.scale(redbin,(100,100))
greensprite=greenbin.get_rect()
greensprite.center=(50,800)
redsprite=redbin.get_rect()
redsprite.center=(950,800)
battery=pygame.image.load('the only batteries .jpeg')
battery=pygame.transform.scale(battery,(80,75))
batterysprite=battery.get_rect()
batterysprite.center=(100,100)
dirtyphone=pygame.image.load('the only musty crusty flipphone home phone .jpeg')
dirtyphone=pygame.transform.scale(dirtyphone,(80,70))
dirtyphonesprite=dirtyphone.get_rect()
dirtyphonesprite.center=(500,100)

while gameloop:
    for event in pygame .event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    screen.fill('blue')
    screen.blit(greenbin, greensprite)
    screen.blit(redbin, redsprite)
    screen.blit(battery, batterysprite)
    screen.blit(dirtyphone, dirtyphonesprite)
    pygame.display.update()
pygame.quit()
  