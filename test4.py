import pianohack
import lessonPlan
import eventInfo
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
lightred = (250,0,0)
clicked = []
clock = pygame.time.Clock()

class MainApp:

	def __init__(self, keyboard, button, lessonPlan, teachingMessages, eventInfo):
		self.keyboard = keyboard
		self.button = button
		self.lessonPlan = lessonPlan
		self.teachingMessages = teachingMessages
		self.eventInfo = eventInfo


def event_test(msg, eventInfo):
    for i in range(MainApp.eventInfo.numKeys()):
        all_equal = True
        while all_equal:
            if(msg.note == MainApp.eventInfo.keyValues[i]):
				return True

def main_screen(inport, port_out, mainApp, eventInfo):
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
            pygame.display.update()
            displayed = True


        msg = getInput(inport)

		print(event_test(msg, eventInfo))

        playNote(msg.note, msg.velocity, inport, port_out)
     #   print(msg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                crash = False


def start_screen(inport, port_out, mainApp, eventInfo):
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
    mainApp = MainApp(None, None, None, None, None)
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

    start_screen(inport, port_out, mainApp, eventInfo)

    del port_out
    pygame.midi.quit()

main()


pygame.quit
exit()
