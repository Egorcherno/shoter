#Создай собственный Шутер!
from pygame import *
from random import randint
font.init()
game = True

W=1366
H=768

ef = True
class Bfg(sprite.Sprite):
    def __init__(self,x,y,pic_name,face,hp):
        super().__init__()
        self.image = image.load(pic_name)
        self.image = transform.scale(self.image,(10,10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.face = face
        self.speed = 5
        self.hp = hp
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Basa(sprite.Sprite):
    def __init__(self,x,y,pic_name,face,hp):
        super().__init__()
        self.image = image.load(pic_name)
        self.image = transform.scale(self.image,(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.face = face
        self.speed = 5
        self.hp = hp
    def reset(self):
        win.blit(self.image,(self.rect.x-30,self.rect.y))


D = 0
F = 0

class Enemy(Basa):
     
    def update(self):
        global D,F,shrift
        global game,o,gamemode
        if self.face == 'dawn':
            self.rect.y+=5
        if self.face == 'left':
            self.rect.x+=5
        if self.face == 'up':
            self.rect.y-=5
        if self.face == 'right':
            self.rect.x-=5

            
        if self.rect.y >= H :
            
            D +=1
            self.rect.y = 0
            self.rect.x = randint(0,W)
            o = shrift.render('ТЫ пропустил ' + str(D) + ' иноплонетянинов',0,(255,255,255))
            print(D)
        if sprite.collide_rect(self,ghost):
            gamemode = 'LOSE'
            print('you loser')
        self.reset()

class Pulya(Bfg):
    def update(self):
        global game
        if self.face == 'up':
          self.rect.y-=5
        self.reset()

attak_pics = ['ufo.png','asteroid.png']
class Boss(Basa):
    global gamemode
    def g_atack (self):
        
        easy = Enemy(0 , W,1,'dawn','150')
        easy1 = Enemy(0 , W,1,'dawn','150')
        if sprite.collide_rect(self,ghost):
                gamemode = 'LOSE'
                print('you loser')
    def v_atack (self):
        
        easy = Enemy(0 , W,2,'dawn','150')
        easy1 = Enemy(0 , W,2,'dawn','150')
        
        if sprite.collide_rect(self,ghost):
                gamemode = 'LOSE'
                print('you loser')
    def update(self):
        WW = W/2

        if sprite.collide_rect(self,ghost):
            gamemode = 'LOSE'
            print('you loser')
        self.reset()

shrift = font.SysFont('Arial',25)
o = shrift.render('ТЫ пропустил ' + '  ' + str(D) + "  "+ ' иноплонетянинов',0,(255,255,255))
o1 = shrift.render('ТЫ убил ' + '  ' + str(F) + "  "+ ' иноплонетянинов',0,(255,255,255))

class Hero(Basa):
    def update(self):
        
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -=  self.speed
        if keys[K_d]:
            self.rect.x +=  self.speed
        if keys[K_LSHIFT]:
            self.speed =  20
        if not keys[K_LSHIFT]:
            self.speed =  5

        if self.rect.x<0:
            self.rect.x+=5
        if self.rect.x>W:
            self.rect.x-= 5

        if self.rect.y<0:
            self.rect.y+=5
        if self.rect.y>H-30:
            self.rect.y -= 5
        self.reset()
    def shoot(self):
        global F,ef,o1
        p = Pulya(self.rect.x,self.rect.y,'bullet.png','up','1')
        pulys.add(p)
        
        


        
enemy_pics = ['ufo.png','asteroid.png']

monst = sprite.Group()
easy = Enemy(randint(100 , W),0,enemy_pics[randint(0,1)],'dawn','1500')
easy1 = Enemy(randint(100 , W),0,enemy_pics[randint(0,1)],'dawn','1500')
easy2= Enemy(randint(100 , W),0,enemy_pics[randint(0,1)],'dawn','1500')
easy3= Enemy(randint(100 , W),0,enemy_pics[randint(0,1)],'dawn','1500')
easy4= Enemy(randint(100 , W),0,enemy_pics[randint(0,1)],'dawn','1500')
easy5= Enemy(randint(100 , W),0,enemy_pics[randint(0,1)],'dawn','1500')
easy6= Enemy(randint(100 , W),0,enemy_pics[randint(0,1)],'dawn','1500')
easy7= Enemy(randint(100 , W),0,enemy_pics[randint(0,1)],'dawn','1500')
easy8= Enemy(randint(100 , W),0,'ufo.png','dawn','1500')
easy9= Enemy(randint(100 , W),0,'ufo.png','dawn','1500')
easy10= Enemy(randint(100 , W),0,'ufo.png','dawn','1500')
easy11= Enemy(randint(100 , W),0,'ufo.png','dawn','1500')
easy12= Enemy(randint(100 , W),0,'ufo.png','dawn','1500')
easy13= Enemy(randint(100 , W),0,'ufo.png','dawn','1500')
easy14= Enemy(randint(0 , W),0,'ufo.png','dawn','1500')
easy15= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy16= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy17= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy18= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy19= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy20 = Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy21 = Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy22= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy23= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy24= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy25= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy26= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy27= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy28= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')
easy29= Enemy(randint(0 , W),randint(100 ,H),'ufo.png','dawn','1500')


ghost = Hero(0,700,'rocket.png','','500')

monst.add(easy)
monst.add(easy1)
monst.add(easy2)
monst.add(easy3)
monst.add(easy4)
monst.add(easy5)
monst.add(easy6)
monst.add(easy7)
monst.add(easy8)
monst.add(easy9)
monst.add(easy10)
monst.add(easy11)
monst.add(easy12)
monst.add(easy14)
monst.add(easy13)
win = display.set_mode((W,H),FULLSCREEN)

display.set_caption("shoot")
bg = image.load("galaxy.jpg")
bg = transform.scale(bg,(W,H))


mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

clock = time.Clock()
FPS = 60


def control():
    global game,gamemode
    for e in event.get():
        if e.type == 2:
            keys = key.get_pressed()
            if keys[K_ESCAPE]:
                game=False
        if e.type == KEYUP:
            if e.key == K_SPACE:
                ghost.shoot()
                print('you shoot')
            if e.key == K_KP_ENTER:
                gamemode = 'PLAY'
                print(e)

pulys = sprite.Group()

font.init()
shift = font.SysFont('Arial',150)
lose = shift.render('You lose',False,(255,0,0))

WIN = shift.render('You Win',False,(0,255,0))


fo = image.load('onn.jpg')
fo = transform.scale(fo,(W,H))
gamemode = "START"
while game :
    
    clock.tick(FPS) 
    control()
    if gamemode == 'START':
        win.blit(fo,(0,0))
    if gamemode == 'PLAY':
        
        win.blit(bg,(0,0))
        win.blit(o,(0,0))
        win.blit(o1,(0,30))
    
       
        monst.update()
        pulys.update()
        ghost.update()
        asa = sprite.groupcollide(monst,pulys,False,True)
        for i in asa:
            i.rect.y = 0
            i.rect.x = randint(0,W)
            F += 1
            o1 = shrift.render('ТЫ убил ' + '  ' + str(F) + "  "+ ' иноплонетянинов',0,(255,255,255))
        else:
            pass
        
    if D >= 75:
        print('you lose')
        gamemode = 'LOSE'
        F = 0
        D = 0

    if gamemode == 'LOSE' :
        for i in monst:
            i.rect.y = 0
        pulys.empty()
        WIN = shift.render('You Lose',False,(0,255,0))
        win.blit(lose,(150,150))
        F = 0
        D = 0

    if F >= 61:
        print('you win')
        WIN = shift.render('You Win',False,(0,255,0))
        win.blit(WIN,(150,150))
        gamemode = 'Win'
    if gamemode == 'Win':
        WIN = shift.render('You Win',False,(0,255,0))
        win.blit(WIN,(150,150))
        for i in monst:
            i.rect.y = 0
        pulys.empty()
        F = 0
        D = 0
    print(D)
    display.update()