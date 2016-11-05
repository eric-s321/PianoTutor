import pygame

pygame.init()
gdisplay = pygame.display.set_mode((600,800))
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
clicked = []
class keyboard(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            pygame.draw.rect(gdisplay, white, (230,100,50,100))
            pygame.draw.rect(gdisplay, black, (230,100,50,100), 1)
            pygame.draw.rect(gdisplay, black, (215,100,30,55))
            
class button(pygame.sprite.Sprite):
     def __init__(self):
        super().__init__()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        
        if 155+100 > mouse[0] > 155 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(gdisplay, red, (155,550, 100, 50))
           
        else:
            pygame.draw.rect(gdisplay, lightred, (155,550, 100, 50))

        font2 = pygame.font.Font("freesansbold.ttf",20)
        btext= font2.render("Start", 1,(0,0,0))
        gdisplay.blit(btext, (160, 560))

  
        
def start_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gdisplay.fill(red)
        font=pygame.font.Font(None,90)
        scoretext=font.render("Placeholder", 10,(0,0,0))
        gdisplay.blit(scoretext, (100, 300))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        button()
        if 155+100 > mouse[0] > 155 and 550+50 > mouse[1] > 550:
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
