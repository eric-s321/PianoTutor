import pygame
import mido
import pygame.midi
import time

mido.set_backend('mido.backends.pygame')
pygame.init()
gdisplay = pygame.display.set_mode((1275,800))
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
clicked = []
clock = pygame.time.Clock()

class keyboard(pygame.sprite.Sprite):
    def __init__(self,ycoord,whiteKeyLeft, whiteKeyRight, whiteWidth, 
            blackWidth, whiteLength, blackKeyLeft, numOctaves):
            print("redrawing keyboard")
            super().__init__()

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
                print("num octvaes is", numOctaves)

#def keyred():
    #if input from keyboard == (coordinates):
        #pygame.draw.rect(gdisplay, red, (coordinates))
            
class button(pygame.sprite.Sprite):
     def __init__(self):
        super().__init__()
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
        
def main_screen(inport, port_out):
    crash = True
    gdisplay.fill(white)

#    def __init__(self,ycoord,whiteKeyLeft, whiteKeyRight, whiteWidth, 
#            blackWidth, whiteLength, blackKeyLeft, numOctaves):
    keyboard(100,10,1250,43,28,175,41,4)
    pygame.display.update()
    while crash:
        msg = getInput(inport)
        playNote(msg.note, msg.velocity, inport, port_out)
     #   print(msg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                crash = False
      
        
def start_screen(inport, port_out):
    intro = True
    # if user clicks x in window the game exits
    while intro:
        gdisplay.fill(white)
        font=pygame.font.Font(None,90)
        scoretext=font.render("Piano Tutor", 10,(0,0,0))
        gdisplay.blit(scoretext, (500, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                intro = False
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        button()
        #if mouse is clicked within area of rectangle the screen changes
        if 500+100 > mouse[0] > 500 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                    clicked.append(button)
        if button in clicked:
            print("in clicked")
            gdisplay.fill(white)
            main_screen(inport, port_out)
            
        
        pygame.display.update()
        clock.tick(60)


def playNote(note, velocity, inport, port_out):

    while velocity != 0:
        port_out.note_on(note, velocity) #64 is the key, 127 is the volume (127 is maximum volume)
     #   time.sleep(.001)
        keyInfo = getInput(inport)
        velocity = keyInfo.velocity
        note = keyInfo.note
    port_out.note_off(note, velocity)

def getInput(inport):
    return inport.receive()


def main():
    pygame.midi.init()
    port_out = pygame.midi.Output(pygame.midi.get_default_output_id()) #creates the
    port_out.set_instrument(0) #sets the instrument to grand piano
    port_out.note_on(60, 0)

    inport = mido.open_input('Keystation 49')

    start_screen(inport, port_out)

    del port_out
    pygame.midi.quit()

main()


pygame.quit
quit()
