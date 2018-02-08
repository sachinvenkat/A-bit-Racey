import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)#fps
pygame.quit()
quit()#for quitting the game


