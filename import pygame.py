import pygame 
pygame.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('my first py game ')
running=True
image1=pygame.image.load('how-to-draw-a-fish-featured-image-1200.png')
image1=pygame.transform.scale(image1,(200,200))
fish=image1.get_rect()
fish.center=(400,400)
image2=pygame.image.load('images.png')
image2=pygame.transform.scale(image2,(300,200))
fish2=image2.get_rect()
fish2.center=(600,600)
image3=pygame.image.load('Unknown.jpeg')
image3=pygame.transform.scale(image3,(800,800))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.blit(image3,(0,0))

    screen.blit(image1,fish)
    screen.blit(image2,fish2)
    pygame.display.update()

pygame.quit()