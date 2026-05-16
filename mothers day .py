import pygame 
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('happy mothers day ')
running=True
image1=pygame.image.load('mothers yay .jpeg')
image1=pygame.transform.scale(image1,(400,400))
happu=image1.get_rect()
happu.center=(200,200)
image2=pygame.image.load('/Users/leodobrov/Pictures/Photos Library.photoslibrary/resources/derivatives/4/4B949353-1A65-47A8-A0AE-63AA3AF1B2EA_1_105_c.jpeg')
image2=pygame.transform.scale(image2,(400,400))
yay=image2.get_rect()
yay.center=(600,600)
image3=pygame.image.load('background for mothers dauy .jpeg')
image3=pygame.transform.scale(image3,(800,800))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.blit(image3,(0,0))

    screen.blit(image1,happu)
    screen.blit(image2,yay)
    pygame.display.update()

pygame.quit()