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
swordsprite.center=(700,600)
bow=pygame.image.load('bow-removebg-preview.png')
bow=pygame.transform.scale(bow,(100,100))
bowsprite=bow.get_rect()
bowsprite.center=(100,600)
staff=pygame.image.load('stafff-removebg-preview.png')
staff=pygame.transform.scale(staff,(100,100))
staffsprite=staff.get_rect()
staffsprite.center=(400,600)
font1=pygame.font.SysFont('Arial',25)
text1=font1.render('match the following',True,"black")
font2=pygame.font.SysFont('Arial',25)
text2=font2.render('result',True,"black")

ns=False
nb=False
nw=False
aS=False
ab=False
aw=False
ws=False
wb=False
ww=False
line1=False
line2=False
line3=False
 

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False 
        if event.type==pygame.MOUSEBUTTONDOWN:
            if ninjasprite.collidepoint(event.pos) and line1==False:
                ns=True
                nw=True
                nb=True
                line1=True
            if archersprite.collidepoint(event.pos) and line2==False:
                aS=True
                aw=True
                ab=True
                line2=True
            if wizardsprite.collidepoint(event.pos) and line3==False:
                ws=True
                ww=True
                wb=True
                line3=True
        if event.type==pygame.MOUSEBUTTONUP:
            if swordsprite.collidepoint(event.pos) and line1==True:
                nb=False
                nw=False
                aS=False
                ws=False
            if swordsprite.collidepoint(event.pos) and line2==True:
                ab=False
                aw=False 
                ns=False 
                ws=False   
            if swordsprite.collidepoint(event.pos) and line3==True:
                wb=False
                ww=False
                aS=False
                ns=False

            if bowsprite.collidepoint(event.pos) and line1==True:
                ns=False
                nw=False
                ab=False
                wb=False
            if bowsprite.collidepoint(event.pos) and line2==True:
                aS=False
                aw=False
                nb=False
                wb=False
            if bowsprite.collidepoint(event.pos) and line3==True:
                ws=False
                ww=False
                nb=False
                ab=False

            if staffsprite.collidepoint(event.pos) and line1==True:
                ns=False
                nb=False
                aw=False
                ww=False
            if staffsprite.collidepoint(event.pos) and line2==True:
                aS=False
                ab=False
                nw=False
                ww=False
            if staffsprite.collidepoint(event.pos) and line3==True:
                ws=False
                wb=False
                nw=False
                aw=False

   # 
   #                 
            
    screen.fill('blue')
    if line1==True:
        if ns:
            pygame.draw.line(screen,'Black',(ninjasprite.centerx,ninjasprite.centery),(swordsprite.centerx,swordsprite.centery),5)
        if nb:
            pygame.draw.line(screen,'Black',(ninjasprite.centerx,ninjasprite.centery),(bowsprite.centerx,bowsprite.centery),5)
        if nw:
            pygame.draw.line(screen,'Black',(ninjasprite.centerx,ninjasprite.centery),(staffsprite.centerx,staffsprite.centery),5)
    if line2==True:
        if aS:
            pygame.draw.line(screen,'Black',(archersprite.centerx,archersprite.centery),(swordsprite.centerx,swordsprite.centery),5)
        if ab:
            pygame.draw.line(screen,'Black',(archersprite.centerx,archersprite.centery),(bowsprite.centerx,bowsprite.centery),5)
        if aw:
            pygame.draw.line(screen,'Black',(archersprite.centerx,archersprite.centery),(staffsprite.centerx,staffsprite.centery),5)
    if line3==True:
        if ws:
            pygame.draw.line(screen,'Black',(wizardsprite.centerx,wizardsprite.centery),(swordsprite.centerx,swordsprite.centery),5)
        if wb:
            pygame.draw.line(screen,'Black',(wizardsprite.centerx,wizardsprite.centery),(bowsprite.centerx,bowsprite.centery),5)
        if ww:
            pygame.draw.line(screen,'Black',(wizardsprite.centerx,wizardsprite.centery),(staffsprite.centerx,staffsprite.centery),5)

    screen.blit(ninja,ninjasprite)
    screen.blit(archer,archersprite)
    screen.blit(wizard,wizardsprite)
    screen.blit(sword,swordsprite)
    screen.blit(bow,bowsprite)
    screen.blit(staff,staffsprite)
    screen.blit(text1,(300,700))
    screen.blit(text2,(300,750))
    pygame.display.update()
pygame.quit()