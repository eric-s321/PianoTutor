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
            print("redrawing keyboard")
            super().__init__()
            x = 180
            
            for i in range(14):
        
                pygame.draw.rect(gdisplay, white, (x,100,50,100))
                pygame.draw.rect(gdisplay, black, (x,100,50,100), 1)
                x += 50
     
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
        
def main_screen():
    crash = True
    gdisplay.fill(white)
    keyboard()
    pygame.display.update()
    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                crash = False
      
        
def start_screen():
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
            gdisplay.fill(white)
            main_screen()
            
        
        pygame.display.update()
        clock.tick(60)
start_screen()




pygame.quit
quit()
