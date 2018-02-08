import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 500
 
black = (0,0,0)#no color, absence of colors(R,G,B)
white = (255,255,255)
red = (255,0,0)
car_width = 73


#game window size
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')#to display the image

def things(thingx,thingy,thingw, thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw, thingh])    
    

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_objects(text,largeText)
    TextRect.center =((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    
    time.sleep(2)

    game_loop()

    


def crash():
    message_display('You Crashed')


    
def game_loop():
    #(x,y)= (0,0)-> top left 
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed= 7
    thing_width = 100
    thing_height = 100
    gameExit = False

    while not gameExit:
        #event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    x_change = -5
                    
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                    x_change = 0
                    


        x += x_change
            
        gameDisplay.fill(white)# upon white display
        
        #things(thingx,thingy,thingw, thingh,color):
        things(thing_startx,thing_starty,thing_width, thing_height,black)
        thing_starty += thing_speed


        car(x,y)               # a car is placed

        if x > display_width-car_width or x<0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
        pygame.display.update()# flip() 
        clock.tick(60)#fps

game_loop()
pygame.quit()
quit()#for quitting the game


