############################################################# SUSHI BOUNCE ####################################################################
################################################### BY: EILEEN ZHANG AND VIANNA VUONG #########################################################
################################################### PICS BY: RESTAURANT CITY (AND V.V) ########################################################
import time
from game import Game
from pygame import *

screen = display.set_mode((600, 800))
init()
bg            = image.load("testing.png")
Mplay         = image.load("play.png")
Minstructions = image.load("instructions.png")
Mhighscore    = image.load("highscores.png")
title         = image.load("sushi.png")
highscorepage = image.load("highscore.png")
PLAYERPIC     = image.load("player.png")
ktn           = image.load("stall.png")
LIVESPIC      = image.load("playerF2.png")
NoLife        = image.load("loselife.png")

fnt       = font.SysFont("Calibri",36)
clock = time.Clock()

lives = 3
def game(screenD):
    global level, timeLeft, score
    # The game fn runs all the functions that are needed for game play.
    running = True
    g = Game(level, screen, lives)
    gameStart = time.get_ticks()
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "HighScorePage"
            if evnt.type == KEYDOWN:
                if evnt.key==27:
                    return "exit"
        timeLeft = 60 - (time.get_ticks() - gameStart)/1000
        keys = key.get_pressed()
#================running all the functions above==========================
        g.move_player()
        g.bounce()
        g.seesaw.rotate()
        if len(g.fruits) != 0:
            g.check_fruits()
            g.move_fruits()
            score += g.collide()
        else:
            g.make_fruits()
        textPic, textTime, textLevel = g.fontt(score, timeLeft)    
        g.drawzIt(textPic, textTime, textLevel)
        if timeLeft<0 and len(g.level.req)>0 and lives<=0: # no time+ingredients leftover+no lives = gameover
            return "gameover"
        elif timeLeft < 0 and lives > 0:               # no time+lives = lose a life screen
            return "lifepg"
        if len(g.level.req) == 0:
            if level == 6:                          # at final level goes directly to highscorepage
                return "HighScorePage"
            elif level < 6:                        # if not at final level, continue to next level
                level += 1
                return "continue"
        clock.tick(120)
    return "menu"

def Continue(screenD):
    '''
    This fn blits the continue screen at the end of each level.
    Bonus score (dependant on time) is added to score and all lists are reset.
    '''
    global fnt, score
    running=True
    pic   = image.load("continue.png")
    continueB = Rect(85,450,452,117)
    quitB     = Rect(85,590,427,140)

    userScore = fnt.render("Score: "+str(score),1,(0,0,0)) # making txt pics
    timeBonus = fnt.render("TIme Bonus: "+str(timeLeft/5),1,(0,0,0))
    totalScore = fnt.render("Total score: "+str(score+timeLeft/5),1,(0,0,0))
    text = [userScore,timeBonus, totalScore]
    score += timeLeft/5 #adds bonus pints
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running=False
            if evnt.type == KEYDOWN:
                if evnt.key==27:
                    return "exit"
        textY = 200
        screen.blit(pic, (0,0))
        mx,my = mouse.get_pos()
        mb    = mouse.get_pressed()
        for i in text:
            screen.blit(i,(100,textY))
            textY += 50
        if continueB.collidepoint(mx,my): 
            draw.rect(screen,(0,148,200),continueB,3)
            if mb[0]==1:
                return "play" # go to next level
        if quitB.collidepoint(mx,my):
            draw.rect(screen,(0,148,200),quitB,3)
            if mb[0]==1:
                return "HighScorePage" # quit and enter highscore
        display.flip()
    return "menu"
#=========================================================================
def LifePage(screenD):
    # Blits on a page that tells user they have lost a life, subtracts life.
    global fnt, score,lives
    lives-=1 # takes life off
    running=True
    retry =Rect(185,630,235,100)
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running=False
            if evnt.type == KEYDOWN:
                if evnt.key==27:
                    return "exit"
        mx,my = mouse.get_pos()
        mb    = mouse.get_pressed()
        if lives<=0:
            return "gameover" # if its the last life, game ends
        else:
            screen.blit(NoLife,(0,0))
            if retry.collidepoint(mx,my):
                draw.rect(screen,(0,148,200),retry,3)
                if mb[0]==1:
                    return "play" #level is run again
        display.flip()
    return "game"    
#==========================================================================
def instructions(screenD):
    # Blitting instruction pages.
    running = True
    pg1     = True 
    pg2     = False
    pic   = image.load("instructbg.png")
    pic2  = image.load("instructbg2.png")
    arrows= [Rect(90,690,88,49),Rect(430,690,88,49),Rect(220,690,144,44)]
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        mx,my = mouse.get_pos()
        mb    = mouse.get_pressed()
        if pg1:
            screen.blit(pic, (0,0))
            if arrows[0].collidepoint(mx,my):
                draw.rect(screen,(0,148,200),arrows[0],3)
                if mb[0]==1:
                    return "menu" # left arrow goes back to menu
            elif arrows[1].collidepoint(mx,my):
                draw.rect(screen,(0,148,200),arrows[1],3)
                if mb[0]==1:
                    pg1=False
                    pg2=True      # right arrow goes to page 2
        if pg2:
            screen.blit(pic2,(0,0))
            if arrows[2].collidepoint(mx,my):
                draw.rect(screen,(0,148,200),arrows[2],3)
                if mb[0]==1:
                    return "menu" # goes to menu
        display.flip()
    return "menu"
#==========================================================================
def highscore(screenD):
    # Creates a huge list of top 11 scorers and blits it.
    running = True
    y = 200
    hsbg = image.load("highscorebg.png")
    screen.blit(hsbg,(0,0))
    highScoreString = ""
    scoreList = open("highscore.txt").read().split('\n')
    if len(scoreList)>10:
        scoreList = scoreList[:11] # takes top 11 scores
    for line in scoreList:
        if line=="" or line.count(",")==0:
            scoreList.remove(line)
        else:
            name1,score1 = line.split(",") 
            highScoreString += name1+"  "+score1
            textMain=fnt.render(highScoreString,1,(100,200,100))
            screen.blit(textMain,(82,y))
            y+=50 # spacing out
            highScoreString = ""
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running=False
            if evnt.type == KEYDOWN:
                if evnt.key==27:
                    return "exit"
            textMain=fnt.render(highScoreString,1,(100,200,100))
            screen.blit(textMain,(20,200))  
            display.flip()
    return "menu"

def ReadingHS(name,score):
    '''
    This fn takes in data from highscore.txt and separates the names and scores
    (which are separated with a comma) into separate lists. It adds in the new
    name and score according to the ranking of the score. The information is
    then all rewritten into highscore.txt so that the information will not be
    lost.
    '''
    global a,scoreList,Reading,x
    x=0 # used to make sure the [name,score] is only written once and on not top of every score its greater than
    scoreList = open("highscore.txt","r").read().split("\n")
    for line in scoreList:
        if line == "":
            scoreList.remove(line)          # gets rid of all empty lines so that error msg disappears
        else:
            name1,score1 = line.split(",")  # separates name and score
            names.append(name1)
            scores.append(score1)
    HS = open("highscore.txt","w")
    for j in range(len(names)):
        if int(scores[j])<=score and x==0:  # writes name if the score is greater than any score i in the list
            HS.write(name+","+str(score)+"\n")
            x = 1
        HS.write(names[j]+","+str(scores[j])+"\n")
    if len(names)==0:
        HS.write(name+","+str(score)+"\n")  # just writes it if nothings in the list
    if x == 0:                                # if hasnt been written yet
        HS.write(name+","+str(score)+"\n")  # write at bottom
    HS.close()

def HighScoreName(screenD):
    # This fn allows the user to enter their name for highscore. (keyboard input)
    global name,names,scores,score,Reading
    names  = []
    scores = []
    name   = ""
    running= True
    cap    = False
    Reading= False
    fnt    = font.SysFont("Calibri",56)
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running=False
            if evnt.type == KEYDOWN:                # ESC; closes entire window
                if evnt.key==27:
                    return "exit"
                if evnt.key==304 or evnt.key==303:  # There are two shift key
                    cap = True                      # If shift is pressed, then allow capitals
                if cap == False:
                    if evnt.key in range (32,126): 
                        name+=chr(evnt.key)         # Adds the letter that the user typed to string
                if cap == True:
                    if evnt.key in range (32,123):
                        name +=chr(evnt.key-32)     # The capital is 32 less that the letter
                        cap=False                   # prevents it from staying in caps
                if evnt.key==8:                     # Backspace
                    name = name[:len(name)-1]       # Gets rid of the last character in string
                if evnt.key==13:                    # ENTER; calls read fn which writes the name+score
                    Reading=True
                    ReadingHS(name,score)
                    return "menu"                   # brings user back to menu
        screen.blit(highscorepage,(0,0))
        textName = fnt.render(name,1,(0,0,0)) 
        screen.blit(textName,(80,490))              # Set name back to nothing
        display.flip()
    return "menu"  
#==========================================================================
def menu(screenD):
    # Returns screen that is chosen by user.
    level = 1   # including level
    score = 0
    running=True
    pg=["play","instructions","highscore"]
    boxes=[Rect(250,350,100,50),Rect(250,450,100,50),Rect(250,550,100,50)]
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "exit"
            if evnt.type == KEYDOWN:
                if evnt.key==27:
                    return "exit"
        screen.blit(bg,(0,0))
        screen.blit(title,(90,150))
        mb   = mouse.get_pressed()
        mx,my= mouse.get_pos()
        screen.blit(Mplay,(250,350))
        screen.blit(Minstructions,(250,450))
        screen.blit(Mhighscore,(250,550))
        for i in range(3):
            if boxes[i].collidepoint((mx,my)):
                draw.rect(screen,(0,144,148),boxes[i],5)
                if mb[0]==1:
                    return pg[i] #returns page user clicked on
        display.flip()

screenD = "menu"
level = 1
score = 0

while screenD != "exit": #what is displayed/run is controlled by what screenD is 
    mb   = mouse.get_pressed()
    if screenD == "menu":
        screenD = menu(screenD)
    if screenD == "instructions":
        screenD = instructions(screenD)
    if screenD == "play":
        screenD = game(screenD)
    if screenD == "highscore":
        screenD = highscore(screenD)
    if screenD == "HighScorePage":
        screenD = HighScoreName(screenD)
    if screenD == "gameover":
        screenD = gameOver(screenD)
    if screenD == "continue":
        screenD = Continue(screenD)
    if screenD == "lifepg":
        screenD = LifePage(screenD)
    
quit()
del fnt