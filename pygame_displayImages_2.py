import pygame

pygame.init()

display_width = 800
display_height = 500
 
black = (0,0,0)#no color, absence of colors(R,G,B)
white = (255,255,255)
red = (255,0,0)
#game window size
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')#to display the image

def car(x,y):
    gameDisplay.blit(carImg,(x,y))
#(x,y)= (0,0)-> top left 
x = (display_width * 0.45)
y = (display_height * 0.8)
    
crashed = False

while not crashed:
    #event handling loop
    for event in pygame.event.get():
        if event.type == pygame.quit:
            crashed = True

    gameDisplay.fill(white)# upon white display     
    car(x,y)               # a car is placed
    pygame.display.update()# flip() 
    clock.tick(60)#fps
pygame.quit()
quit()#for quitting the game


