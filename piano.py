import pygame
import random

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
            
class Player(pygame.sprite.Sprite):
 
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([600, 800])
    
        self.rect = self.image.get_rect()
        
    
            
    def update(self):
        pos = pygame.mouse.get_pos()
 
        self.rect.x = pos[0]
        self.rect.y = 550

    def set_image(self, filename = None):
        if (filename != None):
            self.image = pygame.image.load(filename)
            self.rect = self.image.get_rect()
    
class Apple(pygame.sprite.Sprite):
    image = None
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([30, 40])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
        if Apple.image is None:
            Apple.image = pygame.image.load('apple.png')
        self.image = Apple.image
    def update(self):
        self.rect.y += 3

class yel_apple(pygame.sprite.Sprite):
    image = None
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([30, 40])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
        if yel_apple.image is None:
            yel_apple.image = pygame.image.load('yel_apple.png')
        self.image = yel_apple.image
    def update(self):
        self.rect.y += 8
        
def texts(score):
   font=pygame.font.Font(None,30)
   scoretext=font.render("Score:"+str(score), 1,(0,0,0))
   gdisplay.blit(scoretext, (10, 10))


pygame.init()
gdisplay = pygame.display.set_mode((600,800))
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
lightred = (250,0,0)
blue = (0,0,255)
pygame.display.set_caption("Zombie War")


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

class button(pygame.sprite.Sprite):
     def __init__(self):
        super().__init__()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        
        if 155+100 > mouse[0] > 155 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(gdisplay, red, (155,550, 100, 50))
           
        else:
            pygame.draw.rect(gdisplay, lightred, (155,550, 100, 50))

        if 400+100 > mouse[0] > 400 and 550+50 > mouse[1] > 550:
            pygame.draw.rect(gdisplay, red, (400,550, 120, 50))
        else:
            pygame.draw.rect(gdisplay, lightred, (400,550, 120, 50))

        font2 = pygame.font.Font("freesansbold.ttf",20)
        btext= font2.render("Start", 1,(0,0,0))
        gdisplay.blit(btext, (160, 560))

        font3 = pygame.font.Font("freesansbold.ttf",20)
        btext= font3.render("Load Game", 1,(0,0,0))
        gdisplay.blit(btext, (405, 560))
def keyboard(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            pygame.draw.rect(gisplay, black, (200,600,50,100))


clicked = []       
def start_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gdisplay.fill(white)
        font=pygame.font.Font(None,90)
        scoretext=font.render("Apple Catcher", 10,(0,0,0))
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
        pygame.display.update()
        clock.tick(60)
start_screen()
all_sprites_list = pygame.sprite.Group()
apple_list = pygame.sprite.Group()
yel_list = pygame.sprite.Group()
gdisplay = pygame.display.set_mode((600,800))
pygame.display.set_caption("Apple Catcher")
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
player = Player()
all_sprites_list.add(player)
player.set_image('guy.png')
score = 0

 
x = 0
y = -150
y_change = 0

crashed = False
while not crashed:
    n = 2
    new_list = pygame.sprite.Group()
    new_list.add(player)
    gdisplay.fill(white)
    seconds = int(pygame.time.get_ticks())
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            crashed = True
   
    if seconds % 15 == 0:
            apple = Apple()
            
            apple.rect.x = random.randrange(600)
            apple.rect.y = 0
           
            all_sprites_list.add(apple)
            apple_list.add(apple)
   
    
    if seconds % 243 == 0:
        yel = yel_apple()
        yel.rect.x = random.randrange(600)
        yel.rect.y = 0
        all_sprites_list.add(yel)
        yel_list.add(yel)
    all_sprites_list.update()
    all_sprites_list.draw(gdisplay)
    for apple in apple_list:
        if pygame.sprite.spritecollide(apple, new_list, True):
            apple_list.remove(apple)
            all_sprites_list.remove(apple)
            all_sprites_list.add(player)
            score += 1
    for yel in yel_list:
        if pygame.sprite.spritecollide(yel, new_list, True):
            yel_list.remove(yel)
            all_sprites_list.remove(yel)
            all_sprites_list.add(player)
            score += 10
    texts(score)
    pygame.display.flip()
    clock.tick(100)
pygame.quit
quit()


piano stuff
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