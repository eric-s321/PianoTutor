import pygame
import mido
import pygame.midi
import time

#mido.set_backend('mido.backends.pygame')
#pygame.init()
#gdisplay = pygame.display.set_mode((1275,800))
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
clicked = []
clock = pygame.time.Clock()

class keyboard(pygame.sprite.Sprite):
    def __init__(self,ycoord,whiteKeyLeft, whiteKeyRight, whiteWidth,
            blackWidth, whiteLength, blackKeyLeft, numOctaves, gdisplay):
            print("redrawing keyboard")
            super().__init__()
            self.gdisplay = gdisplay

            keySeperation = whiteWidth
            blackLength = whiteLength * 2/3

            #draw white keys with borders
            for i in range (whiteKeyLeft, whiteKeyRight, +keySeperation):
                pygame.draw.rect(gdisplay, white, (i,ycoord,whiteWidth,whiteLength))
                pygame.draw.rect(gdisplay, black, (i,ycoord,whiteWidth,whiteLength), 1)

            #draw black keys - each outer loop draws on octave
            for i in range (0, numOctaves):
                for j in range (blackKeyLeft,blackKeyLeft + 51, +keySeperation): # draw group of 2 black keys
                    print("j is ", j)
                    pygame.draw.rect(gdisplay, black, (j,ycoord,blackWidth,blackLength))
                blackKeyLeft += keySeperation * 3
                for k in range (blackKeyLeft, blackKeyLeft + 101, +keySeperation): #draw group of 3 black keys * 3
                    print("k is ", k)
                    pygame.draw.rect(gdisplay, black, (k,ycoord,blackWidth,blackLength))
                blackKeyLeft += keySeperation * 4
          #      print("num octvaes is", numOctaves)

#def keyred():
    #if input from keyboard == (coordinates):
        #pygame.draw.rect(gdisplay, red, (coordinates))

class button(pygame.sprite.Sprite):
     def __init__(self, gdisplay):
        super().__init__()
        self.gdisplay = gdisplay
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # if mouse is in button rectangle area the rectangle turns light red
        if 500+100 > mouse[0] > 500 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(gdisplay, red, (500,550, 100, 50))

        else:
            pygame.draw.rect(gdisplay, lightred, (500,550, 100, 50))

        font2 = pygame.font.Font("freesansbold.ttf",20)
        btext= font2.render("Start", 1,(0,0,0))
        gdisplay.blit(btext, (505, 560))
