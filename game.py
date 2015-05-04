############################################################# SUSHI BOUNCE ####################################################################
################################################### BY: EILEEN ZHANG AND VIANNA VUONG #########################################################
################################################### PICS BY: RESTAURANT CITY (AND V.V) ########################################################

from pygame import *
from math import *
from random import *

from player import Player
from fruits import Fruit
from level import Level
from seesaw import Seesaw

PLAYERPIC     = image.load("player.png")
LIVESPIC      = image.load("playerF2.png")
ktn           = image.load("stall.png")

a = 3
b = 7
r1 = Rect(0,140,200,20)                                       # chopstick1
r2 = Rect(400,140,200,20)    

class Game:
    def __init__(self, level, screen, lives):
        self.player1 = Player("p1", 150, 100, -5, False, False, True, False, 0, 150)
        self.player2 = Player("p2", 450, 630, -23, False, False, False, False, 400, 550)
        self.setup(screen)
        self.fruits = []
        self.level = Level(level)
        self.screen = screen
        self.copy = screen.copy()
        self.lives = lives
        self.seesaw = Seesaw()

    # name, x, y, score, direction, speed, special, pic
    def make_fruits(self):
        for i in range(randint(1,5)):                                      #random number of ingredients will be in ingredient list
            z = randint(0,len(self.level.fruitsList)-1)                              #random position is chosen from points
            rand_x = randint(-300,0)
            rand_y = randint(0,11)*30+170   #random position off screen
            speed = randint(a,b)                                #random speed that corresponds to the random position
            f = self.level.fruitsList[z]
            f.x, f.y = rand_x, rand_y
            f.speed = speed
            self.fruits.append(f)
            
        for i in range(randint(1,5)):                                      #same as above
            y = randint(0,len(self.level.fruitsList)-1)      
            rand_x = randint(600,900)
            rand_y = randint(1,10)*30+180
            speed = -randint(a,b)
            f = self.level.fruitsList[y]
            f.x, f.y  = rand_x, rand_y
            f.speed = speed
            self.fruits.append(f)

    def move_fruits(self):
        for j in self.fruits:
            j.move()

    def move_player(self):
        if self.player1.onPlate == True and not self.player1.up:
            self.player1.move()
        if self.player2.onPlate == True and not self.player2.up:
            self.player2.move()

    def check_fruits(self):
        for j in self.fruits:
            if j.x < -300 or j.x > 900:
                self.fruits.remove(j)

    def collide(self):
        score = 0
        box1 = Rect(self.player1.x-25,self.player1.y-50, 85, 80)
        box2 = Rect(self.player2.x-25, self.player2.y-50, 85, 80)
        for i in self.fruits:
            f = Rect(i.x, i.y, 50, 50)
            if f.colliderect(box1) or f.colliderect(box2):
                score += self.find_requ(i)
        return score

    def find_requ(self, fruit):
        self.fruits.remove(fruit)
        for j in self.level.req:
            if fruit.name == j.name:
                self.level.req.remove(j)
        return fruit.score

    def check(self):
        if self.player1.onPlate == True:
            self.player1.down = True
        elif self.player2.onPlate == True:
            self.player2.down = True

    def bounce(self):
        keys = key.get_pressed()
        if keys[K_SPACE]: 
            self.check() # checks if character needs to go up or down
        if self.player1.down == True:
            self.player1.bounceDown(self.player2, self.seesaw)
        elif self.player2.down==True:
            self.player2.bounceDown(self.player1, self.seesaw)
        if self.player1.up == True:
            self.player1.bounceUp(r1)
        elif self.player2.up == True:
            self.player2.bounceUp(r2)

    def fontt(self, score, timeLeft):
        # This fn creates all the text pictures that are blitted during the game.
        fnt      = font.SysFont("Calibri",20)
        text     = "Score: "+str(score)       # creating text
        timeText = "Time Left:"+str(timeLeft)
        LevelText= "Level:"+ str(self.level.num)
        textPic  = fnt.render(text,1,(0,0,0)) # rendering text
        textTime = fnt.render(timeText,1,(0,0,0))
        textLevel= fnt.render(LevelText,1,(0,0,0))
        return (textPic, textTime, textLevel)

    def drawzIt(self, textPic, textTime, textLevel):
        # Blit the pictures on the screen.
        self.screen.blit(self.copy,(0,0))
        #=========seesaw================
        self.seesaw.draw(self.screen)
        #========fruit====================
        for f in self.fruits:
            self.screen.blit(f.pic,(f.x, f.y))   # blits ingredients in list
        #==========players===============
        self.screen.blit(PLAYERPIC,(self.player1.x-25, self.player1.y-50))                          # blits players
        self.screen.blit(PLAYERPIC,(self.player2.x-25, self.player2.y-50))
        #==========timeLeft and score====
        self.screen.blit(textPic, (250,50))                                              # blits all pics made in fontt()
        self.screen.blit(textTime, (250,100))
        self.screen.blit(textLevel,(250,150))
        #==============requirements========
        x = 20
        for i in self.level.req:
            self.screen.blit(i.pic,(x,700))
            x += 50
        #==============Lives=============
        LX=360
        for i in range(self.lives-1):
            self.screen.blit(LIVESPIC,(LX,0))                                            # blits lives
            LX+=60
        display.flip()

    def setup(self, screen):
        screen.blit(ktn,(0,0))
        draw.rect(screen,(255,255,255),r1)                              # drawing chopstick1
        draw.rect(screen,(255,255,255),r2)      