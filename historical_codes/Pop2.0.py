# SmileyPop2.py
import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
YEL=(240,235,0)
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Pop a Smiley')
mousedown = False
keep_going = True
clock = pygame.time.Clock()
pic = pygame.image.load('a_Smiley.bmp')

colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
sprite_list = pygame.sprite.Group()
sprite_list2=pygame.sprite.Group()
pygame.mixer.init() # add sounds
pop = pygame.mixer.Sound("hit.wav")

font = pygame.font.SysFont("Arial", 24)
count_smileys = 0
count_popped = 0
hits=0
misses=0
count=60
_c=0
true_pop=0
class Smiley(pygame.sprite.Sprite):
    pos = (0,0)
    xvel = 1
    yvel = 1
    scale = 100
    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pic
        self.scale = random.randrange(10,100)
        self.image = pygame.transform.scale(self.image, (self.scale,self.scale))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0] - self.scale/2
        self.rect.y = pos[1] - self.scale/2
        self.xvel = xvel
        self.yvel = yvel

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.xvel = -self.xvel*0.95
        if self.rect.y <= 0 or self.rect.y > screen.get_height() - self.scale:
            self.yvel = -self.yvel*0.95

while keep_going:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            keep_going = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1: # F1 = cheat/pop all smileys
                count_popped += len(sprite_list)
                sprite_list = pygame.sprite.Group() # clear sprite_list
                pop.play()
            if event.key==pygame.K_F12:
                keep_going=False
            
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: # regular left mouse button, draw
                mousedown = True
            elif pygame.mouse.get_pressed()[2]: # right mouse button, pop
                pos = pygame.mouse.get_pos()
                clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                sprite_list.remove(clicked_smileys)
                if len(clicked_smileys)> 0:
                    pop.play()
                    count_popped += len(clicked_smileys)
                    true_pop+=len(clicked_smileys)
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if _c==0:
        screen.fill(BLACK)
    else:
        screen.fill(YEL)
    sprite_list.update()
    sprite_list.draw(screen)
    clock.tick(60)
    if _c==0:
        draw_string = "Bubbles created: " + str(count_smileys)
        draw_string += " - Bubbles popped: " + str(count_popped)
        if (count_smileys > 0):
            draw_string += " - Percent: "
            draw_string += str( round(count_popped*100/count_smileys, 2)) + "%"
    count+=1
    text = font.render(draw_string , True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit (text, text_rect)

    # Hit/Miss counter
    
    pygame.display.update()
    if (count>=60)&(_c==0):
        speedx = random.randint(-5, 5)
        speedy = random.randint(-5, 5)
        _x=random.randint(0,800)
        _y=random.randint(0,600)
        count=0
        newSmiley = Smiley(pygame.mouse.get_pos(), speedx, speedy)
        sprite_list.add(newSmiley)
        count_smileys += 1
    
            

        
pygame.quit()
