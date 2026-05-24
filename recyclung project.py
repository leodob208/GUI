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
plasticwaterbottle=pygame.image.load('the only plastic water .jpeg')
plasticwaterbottle=pygame.transform.scale(plasticwaterbottle,(80,75))
plasticwaterbottlesprite=plasticwaterbottle.get_rect()
plasticwaterbottlesprite.center=(850,100)
plasticbag=pygame.image.load('the only plastic bag .jpeg')
plasticbag=pygame.transform.scale(plasticbag,(80,75))
plasticbagsprite=plasticbag.get_rect()
plasticbagsprite.center=(200,100)
draggingplasticbag=False
draggingplasticbottle=False
draggingdirtyphone=False
draggingbattery=False

while gameloop:
    for event in pygame .event.get():
        if event.type==pygame.QUIT:
            gameloop=False
            

        if event.type==pygame.MOUSEBUTTONDOWN:
            if plasticbagsprite.collidepoint(event.pos):
                draggingplasticbag=True
            elif plasticwaterbottlesprite.collidepoint(event.pos):
                draggingplasticbottle=True
            elif dirtyphonesprite.collidepoint(event.pos):
                draggingdirtyphone=True
            elif batterysprite.collidepoint(event.pos):
                draggingbattery=True
        if event.type==pygame.MOUSEMOTION:
            if draggingplasticbag:
                plasticbagsprite.center=event.pos
            elif draggingplasticbottle:
                plasticwaterbottlesprite.center=event.pos
            elif draggingdirtyphone:
                dirtyphonesprite.center=event.pos
            elif draggingbattery:
                batterysprite.center=event.pos
        if event.type==pygame.MOUSEBUTTONUP:
            draggingplasticbag=False
            draggingplasticbottle=False
            draggingdirtyphone=False
            draggingbattery=False
        
    if plasticbagsprite.colliderect(greensprite):
        print('plastic bag recycled')
        plasticbagsprite.center=(1200,1200)
    if batterysprite.colliderect(redsprite):
        batterysprite.center=(1200,1200)
    if dirtyphonesprite.colliderect(redsprite):
        dirtyphonesprite.center=(1200,1200)
    if plasticwaterbottlesprite.colliderect(greensprite):
        plasticwaterbottlesprite.center=(1200,1200)

    screen.fill('blue')
    screen.blit(greenbin, greensprite)
    screen.blit(redbin, redsprite)
    screen.blit(battery, batterysprite)
    screen.blit(dirtyphone, dirtyphonesprite)
    screen.blit(plasticwaterbottle, plasticwaterbottlesprite)
    screen.blit(plasticbag, plasticbagsprite)
    pygame.display.update()
pygame.quit()
  