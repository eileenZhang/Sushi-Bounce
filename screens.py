from pygame import *

def Continue(screenD):
    '''
    This fn blits the continue screen at the end of each level.
    Bonus score (dependant on time) is added to score and all lists are reset.
    '''
    global textPic, fnt, score
    reset()
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
    '''
    Blits on a page that tells user they have lost a life, subtracts life.
    '''
    global textPic, fnt, score,lives
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
    '''
    Blitting instruction pages.
    '''
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
    '''
    Creates a huge list of top 11 scorers and blits it.
    '''
    global highScoreString
    running = True
    y = 200
    hsbg=image.load("highscorebg.png")
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
#==========================================================================
def menu(screenD):
    '''
    Returns screen that is chosen by user.
    '''
    
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
        display.wait(50)