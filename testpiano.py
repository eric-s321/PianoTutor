import mido
import pygame
import pygame.midi
import time

mido.set_backend('mido.backends.pygame')


def playNote(note, velocity, inport):
    port_out = pygame.midi.Output(pygame.midi.get_default_output_id()) #creates the
    port_out.set_instrument(0) #sets the instrument to grand piano
    while velocity != 0:
        port_out.note_on(note, velocity) #64 is the key, 127 is the volume (127 is maximum volume)
        time.sleep(.001)
        keyInfo = getInput(inport)
        velocity = keyInfo.velocity
    port_out.note_off(note, velocity)

def getInput(inport):
    return inport.receive()

def main():
    pygame.midi.init()

    inport = mido.open_input('Keystation 49')
    while True:
        msg = getInput(inport)
        playNote(msg.note, msg.velocity, inport)
        print(msg)
    del port_out
    pygame.midi.quit()

main()
