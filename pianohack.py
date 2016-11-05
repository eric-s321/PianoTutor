import pygame

pygame.init()
gdisplay = pygame.display.set_mode((1000,800))
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
clicked = []
clock = pygame.time.Clock()
class keyboard(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            pygame.draw.rect(gdisplay, white, (180,100,50,100))
            pygame.draw.rect(gdisplay, black, (180,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (230,100,50,100))
            pygame.draw.rect(gdisplay, black, (230,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (280,100,50,100))
            pygame.draw.rect(gdisplay, black, (280,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (330,100,50,100))
            pygame.draw.rect(gdisplay, black, (330,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (380,100,50,100))
            pygame.draw.rect(gdisplay, black, (380,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (430,100,50,100))
            pygame.draw.rect(gdisplay, black, (430,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (480,100,50,100))
            pygame.draw.rect(gdisplay, black, (480,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (530,100,50,100))
            pygame.draw.rect(gdisplay, black, (530,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (580,100,50,100))
            pygame.draw.rect(gdisplay, black, (580,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (630,100,50,100))
            pygame.draw.rect(gdisplay, black, (630,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (680,100,50,100))
            pygame.draw.rect(gdisplay, black, (680,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (730,100,50,100))
            pygame.draw.rect(gdisplay, black, (730,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (780,100,50,100))
            pygame.draw.rect(gdisplay, black, (780,100,50,100), 1)
            pygame.draw.rect(gdisplay, white, (830,100,50,100))
            pygame.draw.rect(gdisplay, black, (830,100,50,100), 1)
            pygame.draw.rect(gdisplay, black, (220,100,30,55))
            pygame.draw.rect(gdisplay, black, (270,100,30,55))
            pygame.draw.rect(gdisplay, black, (370, 100, 30,55))
            pygame.draw.rect(gdisplay, black, (420,100,30,55))
            pygame.draw.rect(gdisplay, black, (470, 100, 30,55))
            pygame.draw.rect(gdisplay, black, (570,100,30,55))
            pygame.draw.rect(gdisplay, black, (670,100,30,55))
            pygame.draw.rect(gdisplay, black, (770, 100, 30,55))
            pygame.draw.rect(gdisplay, black, (820,100,30,55))
            pygame.draw.rect(gdisplay, black, (620, 100, 30,55))

class button(pygame.sprite.Sprite):
     def __init__(self):
        super().__init__()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        if 500+100 > mouse[0] > 500 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(gdisplay, red, (500,550, 100, 50))

        else:
            pygame.draw.rect(gdisplay, lightred, (500,550, 100, 50))

        font2 = pygame.font.Font("freesansbold.ttf",20)
        btext= font2.render("Start", 1,(0,0,0))
        gdisplay.blit(btext, (505, 560))



def start_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                intro = False

        gdisplay.fill(white)
        font=pygame.font.Font(None,90)
        scoretext=font.render("Placeholder", 10,(0,0,0))
        gdisplay.blit(scoretext, (100, 300))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        button()
        if 500+100 > mouse[0] > 500 and 550+50 > mouse[1] > 550:
            if click == (1,0,0):
                    clicked.append(button)
        if button in clicked:
            gdisplay.fill(white)
            return
        keyboard()
        pygame.display.update()
        clock.tick(60)
start_screen()
pygame.quit
quit()
