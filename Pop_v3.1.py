# SmileyPop3.py
#In diffrent stages
import pygame
import random
BLACK = (0,0,0)
WHITE = (255,255,255)
YEL=(240,235,0)
RED=(255,0,0)
pygame.init()
keep_going1=1
def easy():
    
    screen = pygame.display.set_mode([1024, 768])
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
    win=pygame.mixer.Sound('win.wav')
    over=pygame.mixer.Sound('over.wav')
    pl=pygame.mixer.Sound('pl.wav')
    font = pygame.font.SysFont("Arial", 24)
    count_smileys = 0
    count_popped = 0
    hits=0
    misses=0
    count=60
    _c=0
    true_pop=0
    restart=0
    dienum=random.randint(15,35)
    xx=(random.randint(1,1020))
    yy=(random.randint(1,765))
    

    class Smiley(pygame.sprite.Sprite):
        pos = (0,0)
        xvel = 1
        yvel = 1
        scale = 100
        def __init__(self, pos, xvel, yvel):
            pygame.sprite.Sprite.__init__(self)
            self.image = pic
            self.scale = random.randrange(15,100)
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
                    if len(sprite_list)>5:
                        true_pop += 1
                    sprite_list = pygame.sprite.Group() # clear sprite_list
                    pop.play()
                if event.key==pygame.K_F12: #exit
                    pygame.quit()
                if event.key==pygame.K_F4: #restart
                    sprite_list = pygame.sprite.Group() 
                    pop.play()
                    count_popped=0
                    count_smileys=0
                    count=0
                    true_pop=0
                    dienum=random.randint(15,35)
                    _c=0
                    
                    
            if event.type == pygame.MOUSEBUTTONDOWN: #both button to pop
                if pygame.mouse.get_pressed()[0]:                 
                    pos = pygame.mouse.get_pos()
                    clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                    sprite_list.remove(clicked_smileys)
                    if len(clicked_smileys)> 0:
                        pop.play()
                        count_popped += len(clicked_smileys)
                        true_pop+=len(clicked_smileys)
                elif pygame.mouse.get_pressed()[2]: 
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
            pl.play()
        elif(_c>0):
            screen.fill(YEL)
            draw_string="YOU WIN!!!!!!!!!! Percent:"+str( round(true_pop*100/count_smileys, 1))+"%"+"  Lv.2 will start in "
            draw_string+=str(7-int(count/60))
            draw_string+=" seconds."
        else:
            screen.fill(RED)
        pygame.draw.rect(screen,RED,(xx,yy,10,10))
        sprite_list.update()
        sprite_list.draw(screen)
        clock.tick(60)
        if _c==0:
            draw_string = "(lv.1)Bubbles created: " + str(count_smileys)
            draw_string += " - Bubbles popped: " + str(int(count_popped))
            if (count_smileys > 0):
                draw_string += " - Percent: "
                draw_string += str( round(count_popped*100/count_smileys, 2)) + "%"
        count+=1
        text = font.render(draw_string , True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 10
        screen.blit (text, text_rect)

        
        pygame.display.update()
        if (count>=70)&(_c==0):
            speedx = random.randint(-4, 4)
            speedy = random.randint(-4, 4)
            _x=random.randint(0,800)
            _y=random.randint(0,600)
            count=0
            newSmiley = Smiley(pygame.mouse.get_pos(), speedx, speedy)
            sprite_list.add(newSmiley)
            count_smileys += 1
        if (count>=450)&(_c>0):
            n()
        if count_smileys>0:
            if (count_smileys>=50)&((true_pop*100/count_smileys)>75)&(_c==0):
                pl.stop() 
                sprite_list = pygame.sprite.Group() #win
                win.play()
                draw_string="YOU WIN!!!!!!!!!! Percent:"+str( round(true_pop*100/count_smileys, 1))+("%")
                _c+=1
                
            if ((count_smileys>=dienum)&((true_pop*100/count_smileys)<35)&(_c==0)):
                pl.stop()
                sprite_list = pygame.sprite.Group() # lose
                over.play()
                draw_string="You lose, "
                if ((count_popped*100/count_smileys)>50):
                    draw_string+="because you have cheated."
                else:
                    draw_string="You lose!!! In "+str(count_smileys)+" bubbles,you have only popped "+str(count_popped)+" bubbles."
                _c-=1
            if [s for s in sprite_list if s.rect.collidepoint(xx,yy)]:
                pl.stop()
                sprite_list = pygame.sprite.Group() # lose
                over.play()
                draw_string="You lose,because you hit the bomb."
                _c-=1




def h():
    
    screen = pygame.display.set_mode([1024, 768])
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
    win=pygame.mixer.Sound('win.wav')
    over=pygame.mixer.Sound('over.wav')
    pl=pygame.mixer.Sound('pl.wav')
    font = pygame.font.SysFont("Arial", 24)
    count_smileys = 0
    count_popped = 0
    hits=0
    misses=0
    count=40
    _c=2
    true_pop=0
    restart=0
    dienum=random.randint(10,30)
    xx=(random.randint(1,1020))
    yy=(random.randint(1,765))
  

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
                    if len(sprite_list)>5:
                        true_pop += 1
                    sprite_list = pygame.sprite.Group() # clear sprite_list
                    pop.play()
                if event.key==pygame.K_F12: #exit
                    pygame.quit()
                if event.key==pygame.K_F4: #restart
                    sprite_list = pygame.sprite.Group() 
                    pop.play()
                    count_popped=0
                    count_smileys=0
                    count=40
                    true_pop=0
                    dienum=random.randint(10,30)
                    _c=2
                    
                    
            if event.type == pygame.MOUSEBUTTONDOWN: #both button to pop
                if pygame.mouse.get_pressed()[0]:                 
                    pos = pygame.mouse.get_pos()
                    clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                    sprite_list.remove(clicked_smileys)
                    if len(clicked_smileys)> 0:
                        pop.play()
                        count_popped += len(clicked_smileys)
                        true_pop+=len(clicked_smileys)
                elif pygame.mouse.get_pressed()[2]: 
                    pos = pygame.mouse.get_pos()
                    clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                    sprite_list.remove(clicked_smileys)
                    if len(clicked_smileys)> 0:
                        pop.play()
                        count_popped += len(clicked_smileys)
                        true_pop+=len(clicked_smileys)
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
        
        if _c==2:
            screen.fill(BLACK)
            pl.play()
        elif(_c>2):
            screen.fill(YEL)
        else:
            screen.fill(RED)
        pygame.draw.rect(screen,RED,(xx,yy,10,10))
        sprite_list.update()
        sprite_list.draw(screen)
        clock.tick(60)
        if _c==2:
            draw_string = "(lv.3)Bubbles created: " + str(count_smileys)
            draw_string += " - Bubbles popped: " + str(int(count_popped))
            if (count_smileys > 0):
                draw_string += " - Percent: "
                draw_string += str( round(count_popped*100/count_smileys, 2)) + "%"
        count+=1
        text = font.render(draw_string , True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 10
        screen.blit (text, text_rect)

        
        pygame.display.update()
        if (count>=40)&(_c==2):
            speedx = random.randint(-6, 6)
            speedy = random.randint(-6, 6)
            _x=random.randint(0,800)
            _y=random.randint(0,600)
            count=0
            newSmiley = Smiley(pygame.mouse.get_pos(), speedx, speedy)
            sprite_list.add(newSmiley)
            count_smileys += 1
        if count_smileys>0:
            if (count_smileys>=100)&((true_pop*100/count_smileys)>90)&(_c==2):
                pl.stop()
                sprite_list = pygame.sprite.Group() #win
                win.play()
                draw_string="YOU WIN!!!!!!!!!! Percent:"+str( round(true_pop*100/count_smileys, 1))+("%")
                _c+=1
            if ((count_smileys>=dienum)&((true_pop*100/count_smileys)<55)&(_c==2)):
                pl.stop()
                sprite_list = pygame.sprite.Group() # lose
                over.play()
                draw_string="You lose, "
                if ((count_popped*100/count_smileys)>60):
                    draw_string+="because you have cheated."
                else:
                    draw_string="You lose!!! In "+str(count_smileys)+" bubbles,you have only popped "+str(count_popped)+" bubbles."
                _c-=1
            if [s for s in sprite_list if s.rect.collidepoint(xx,yy)]:
                pl.stop()
                sprite_list = pygame.sprite.Group() # lose
                over.play()
                draw_string="You lose,because you hit the bomb."
                _c-=1




def n():
    
    screen = pygame.display.set_mode([1024, 768])
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
    win=pygame.mixer.Sound('win.wav')
    over=pygame.mixer.Sound('over.wav')
    pl=pygame.mixer.Sound('pl2.wav')
    font = pygame.font.SysFont("Arial", 24)
    count_smileys = 0
    count_popped = 0
    hits=0
    misses=0
    count=50
    _c=1
    true_pop=0
    restart=0
    dienum=random.randint(10,35)
    xx=(random.randint(1,1020))
    yy=(random.randint(1,765))
 
    class Smiley(pygame.sprite.Sprite):
        pos = (0,0)
        xvel = 1
        yvel = 1
        scale = 100
        def __init__(self, pos, xvel, yvel):
            pygame.sprite.Sprite.__init__(self)
            self.image = pic
            self.scale = random.randrange(13,100)
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
                    if len(sprite_list)>5:
                        true_pop += 1
                    sprite_list = pygame.sprite.Group() # clear sprite_list
                    pop.play()
                if event.key==pygame.K_F12: #exit
                    pygame.quit()
                if event.key==pygame.K_F4: #restart
                    sprite_list = pygame.sprite.Group() 
                    pop.play()
                    count_popped=0
                    count_smileys=0
                    count=0
                    true_pop=0
                    dienum=random.randint(10,35)
                    _c=1
                    
                    
            if event.type == pygame.MOUSEBUTTONDOWN: #both button to pop
                if pygame.mouse.get_pressed()[0]:                 
                    pos = pygame.mouse.get_pos()
                    clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                    sprite_list.remove(clicked_smileys)
                    if len(clicked_smileys)> 0:
                        pop.play()
                        count_popped += len(clicked_smileys)
                        true_pop+=len(clicked_smileys)
                elif pygame.mouse.get_pressed()[2]: 
                    pos = pygame.mouse.get_pos()
                    clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                    sprite_list.remove(clicked_smileys)
                    if len(clicked_smileys)> 0:
                        pop.play()
                        count_popped += len(clicked_smileys)
                        true_pop+=len(clicked_smileys)
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
        
        if _c==1:
            screen.fill(BLACK)
            pl.play()
        elif(_c>1):
            screen.fill(YEL)
            draw_string="YOU WIN!!!!!!!!!! Percent:"+str( round(true_pop*100/count_smileys, 1))+"%"+"  Lv.2 will start in "
            draw_string+=str(int(8-count/60))
            draw_string+=" seconds."
        else:
            screen.fill(RED)
        pygame.draw.rect(screen,RED,(xx,yy,10,10))
        sprite_list.update()
        sprite_list.draw(screen)
        clock.tick(60)
        
        if _c==1:
            draw_string = "(lv.2)Bubbles created: " + str(count_smileys)
            draw_string += " - Bubbles popped: " + str(int(count_popped))
            if (count_smileys > 0):
                draw_string += " - Percent: "
                draw_string += str( round(count_popped*100/count_smileys, 2)) + "%"
        count+=1
        text = font.render(draw_string , True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 10
        screen.blit (text, text_rect)

        
        pygame.display.update()
        if (count>=50)&(_c==1):
            speedx = random.randint(-5, 5)
            speedy = random.randint(-5, 5)
            _x=random.randint(0,800)
            _y=random.randint(0,600)
            count=0
            newSmiley = Smiley(pygame.mouse.get_pos(), speedx, speedy)
            sprite_list.add(newSmiley)
            count_smileys += 1
        if (count>=460)&(_c>1):
            h()
        if count_smileys>0:
            if (count_smileys>=80)&((true_pop*100/count_smileys)>85)&(_c==1):
                pl.stop()
                sprite_list = pygame.sprite.Group() #win
                win.play()
                draw_string="YOU WIN!!!!!!!!!! Percent:"+str( round(true_pop*100/count_smileys, 1))+"%"
                _c+=1
                
            if ((count_smileys>=dienum)&((true_pop*100/count_smileys)<45)&(_c==1)):
                pl.stop()
                sprite_list = pygame.sprite.Group() # lose
                over.play()
                draw_string="You lose, "
                if ((count_popped*100/count_smileys)>52):
                    draw_string+="because you have cheated."
                else:
                    draw_string="You lose!!! In "+str(count_smileys)+" bubbles,you have only popped "+str(count_popped)+" bubbles."
                _c-=1
            if [s for s in sprite_list if s.rect.collidepoint(xx,yy)]:
                pl.stop()
                sprite_list = pygame.sprite.Group() # lose
                over.play()
                draw_string="You lose,because you hit the bomb."
                _c-=1
                



while keep_going1:
    easy()
    
        
pygame.quit()
