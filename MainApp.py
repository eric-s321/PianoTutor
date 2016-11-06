import pianohack
import lessonPlan
import sys
import pygame
import mido

gdisplay = pygame.display.set_mode((1275,800))
#print("oringal g display", gdisplay)
mido.set_backend('mido.backends.pygame') #sets backend for mido as pygame
pygame.init()
#gdisplay = pygame.display.set_mode((1275,800))
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
blue = (0,0,255)
lightred = (250,0,0)
clicked = []
clock = pygame.time.Clock()

class MainApp:

    def __init__(self, keyboard, button, lessonPlan, teachingMessages):
        self.keyboard = keyboard
        self.button = button
        self.lessonPlan = lessonPlan
        self.teachingMessages = teachingMessages

# def event_test(msg):
#     for i in range(MainApp.eventInfo.numKeys()):
#         all_equal = True
#         while all_equal:
#             if(msg.note == MainApp.eventInfo.keyValues[i]):
#                 return True

def dictwhite():
    dict1 = {'c1':(10,100,43,175),'d1':(53,100,43,175),'e1':(96,100,43,175),'f1':(10,100,43,175),'g1':(139,100,43,175),'a1':(182,100,43,175),'b1':(225,100,43,175),'c2':(10,100,43,175),'d2':(268,100,43,175),'e2':(311,100,43,175),'f2':(354,100,43,175),'g2':(397,100,43,175),'a2':(440,100,43,175),'b2':(483,100,43,175),'c3':(526,100,43,175),'d3':(579,100,43,175),'e3':(612,100,43,175),'f3':(655,100,43,175),'g3':(698,100,43,175),'a3':(741,100,43,175),'b3':(784,100,43,175),'c4':(827,100,43,175),'d4':(870,100,43,175),'e4':(913,100,43,175),'f4':(956,100,43,175),'g4':(999,100,43,175),'a4':(1042,100,43,175),'b4':(1085,100,43,175),}
    return dict1

def dictblack():
    dict2 = {'c1sharp':(41,100,28,117),'d1sharp':(94,100,28,117),'f1sharp':(143,100,28,117),'g1sharp':(194,100,28,117),'a1sharp':(245,100,28,117),'c2sharp':(296,100,28,117),'d2sharp':(347,100,28,117),'f2sharp':(398,100,28,117),'g2sharp':(449,100,28,117),'a2sharp':(500,100,28,117),'c3sharp':(551,100,28,117),'d3sharp':(602,100,28,117),'f3sharp':(653,100,28,117),'g3sharp':(702,100,28,117),'a3sharp':(755,100,28,117),'c4sharp':(806,100,28,117),'d4sharp':(857,100,28,117),'f4sharp':(908,100,28,117),'g4sharp':(959,100,28,117),'a4sharp':(1010,100,28,117)}
    return dict2

def keychange(note,note2):
    dict1 = dictwhite()
    dict2 = dictblack()
    coordinates = (dict1[note])
    coordinates2 = (dict2[note2])
    pygame.draw.rect(gdisplay, blue, coordinates)
    pygame.draw.rect(gdisplay, black, coordinates,1)
    pygame.draw.rect(gdisplay, black, coordinates2)

def main_screen(inport, port_out, mainApp):
    crash = True
    gdisplay.fill(white)

#    def __init__(self,ycoord,whiteKeyLeft, whiteKeyRight, whiteWidth,
#            blackWidth, whiteLength, blackKeyLeft, numOcmtaves):
    mainApp.keyboard = pianohack.keyboard(100,10,1250,43,28,175,41,4, gdisplay)
    pygame.display.update()

    displayed = False
    while crash:

        if not displayed:
            print ("writing to screen")
            mainApp.lessonPlan.writeToScreen(mainApp.teachingMessages[0], 400, 400, 35, gdisplay)
            keychange('c1','c1sharp')
            keychange('e1', 'd1sharp')
            keychange('g1','f1sharp')
            pygame.display.update()
            displayed = True


        msg = getInput(inport)
        playNote(msg.note, msg.velocity, inport, port_out)
     #   print(msg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                crash = False


def start_screen(inport, port_out, mainApp):
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
                sys.exit()
                intro = False

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        mainApp.button = pianohack.button(gdisplay)
        #if mouse is clicked within area of rectangle the screen changes
        if 500+100 > mouse[0] > 500 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                    clicked.append(mainApp.button)
        if mainApp.button in clicked:
            print("in clicked")
            gdisplay.fill(white)
            main_screen(inport, port_out, mainApp)


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
    mainApp = MainApp(None, None, None, None)
    mainApp.teachingMessages = open("teachingMessages.txt", "r").readlines()
    mainApp.lessonPlan = lessonPlan.lessonPlan(gdisplay)
 #   print(mainApp.lessonPlan.gdisplay)
 #   message = mainApp.teachingMessages[0]
 #   mainApp.lessonPlan.writeToScreen("test",500,600,25, gdisplay)
#    mainApp.lessonPlan.test(1,2)
  #  for line in mainApp.teachingMessages:
  #       print(line)
    pygame.midi.init()
    port_out = pygame.midi.Output(pygame.midi.get_default_output_id()) #find the ID
    port_out.set_instrument(0) #sets the instrument to grand piano
    port_out.note_on(60, 0) #plays initial hidden note to decrease delay

    inport = mido.open_input('Keystation 49') #sets input port for mido

    start_screen(inport, port_out, mainApp)

    del port_out
    pygame.midi.quit()

main()


pygame.quit
exit()
