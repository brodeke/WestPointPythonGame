import pygame, sys, time
from pygame.locals import *



##########################################################
WELCOMESCREEN = 0
CAinit = 11
CENTRALAREA = 1
HAYES = 2
MICHIE = 3
THAYER = 4
CSTORE = 5
WIN = 100
CHARSELECT = 37
THinit = 333
CSinit = 555
MSinit = 777
HAinit = 444

gotBelt=False
gotHW=False
gotCAC=False
gotPMI = False
moveRequest = None


HEALTH = 100


BLUE =     (0,   0,   255)
GREEN =    (0,   128, 0)
PURPLE =   (128, 0,   128)
RED =      (255, 0,   0)
YELLOW =   (255, 255, 0)
NAVYBLUE = (0,   0,   128)
WHITE =    (255, 255, 255)
BLACK =    (0,   0,   0)
##########################################################






############################################################



######## MOVECHAR: MOVEMENT FUNCTION, ALSO DESIGNATES AREA BOUNDARIES AND MOVING BOUNDARIES
    
def moveChar(currentArea,charx, chary, event):
        
    moveRequest = False
    
###########Area designator for Central Area: CA
    CAarea1 = chary > 100 and chary < 220 and charx < 614
    CAarea2 = charx < 89 and chary > 222 and chary < 510
    CAarea3 = charx > 220 and chary > 219 and chary < 330
    CAarea4 = charx > 340 and charx < 460 and chary > 329
    CAarea5 = charx > 90 and charx < 341 and chary > 500
    
    CACS = charx > 115 and charx < 205 and chary <105
    CATH = charx < 89 and chary > 509
    CAHY = charx > 613 and chary > 100 and chary < 220  
    CABB = charx > 365 and charx < 429 and chary < 101

###########Area designator for Thayer Hall: TH
        
    THarea1 = chary > 100 and chary <220 and charx < 800
    THarea2 = chary > 219 and chary <320 and charx > 242 and charx < 530
    THarea3 = chary > 219 and chary < 354 and charx < 321
    THarea4 = chary > 353 and chary < 475 and charx > 155 and charx < 240
    THarea5 = chary > 420 and chary < 600 and charx < 156
    THarea6 = chary > 528 and chary < 600 and charx > 155 and charx < 300
    THarea7 = chary > 319 and chary < 600 and charx > 299 and charx < 410
    THarea8 = charx > 409 and charx <460 and chary > 445 and chary < 600
    
    THCA = charx > 529 and charx < 800 and chary > 219 and chary < 330
    THCS = charx > 115 and charx < 205 and chary <105
                  
##########Area designator for Michie Stadium: MS

    MSarea1 = charx > 187 and chary <137 and charx < 800
    MSarea2 = chary > 136 and chary <355 and charx < 800
    MSarea3 = chary > 354 and chary < 600 and charx < 470
    
    MSHY = charx < 187 and charx > 0 and chary > 0 and chary < 137

##########Area designator for Cadet Store: CS
    CSarea1 = charx > 0 and charx < 450 and chary > 0 and chary < 100
    CSarea2 = charx > 305 and chary > 99 and chary < 168
    CSarea3 = charx > 500 and charx < 800 and chary > 167 and chary < 355
    CSarea4 = charx > 305 and charx < 430 and chary > 167 and chary < 394
    CSarea5 = charx > 138 and charx < 306 and chary > 318 and chary < 394
    CSarea6 = charx > 138 and charx < 265 and chary > 214  and chary < 319
    CSarea7 = charx > 0 and charx < 265 and chary > 150 and chary < 215
    CSarea8 = charx > 0 and charx < 106 and chary > 214  and chary < 600
    CSarea9 = charx > 105 and charx < 268 and chary > 444  and chary < 600
    
    CSCA = charx > 267 and charx < 474 and chary > 444 and chary < 600

##########Area designator for Hayes: HY
    HAarea1 = charx > 0 and charx < 150 and chary > 100 and chary < 235
    HAarea2 = charx > 675 and charx < 800 and chary > 100 and chary < 235
    HAarea3 = charx > 0 and charx < 800 and chary > 235 and chary < 280
    HAarea4 = charx > 0 and charx < 615 and chary > 279 and chary < 355
    HAarea5 = charx > 0 and charx < 474 and chary > 354 and chary < 420
    HAarea6 = charx > 435 and charx < 474 and chary > 419 and chary < 485
    HAarea7 = charx > 614 and charx < 800 and chary > 279 and chary < 355

    HAMS = charx > 0 and charx < 450 and chary > 0 and chary < 100
    HACA = charx > 0 and charx < 160 and chary > 484 and chary < 600

################################################################################

############################# MOVEMENT FOR CENTRAL AREA ########################
    if currentArea == CENTRALAREA:
        if CAarea1 or CAarea2 or CAarea3 or CAarea4 or CAarea5 == True:
            if event.key == K_RIGHT:
                charx += 15
            if event.key == K_LEFT:
                    charx -= 15
            if event.key == K_DOWN:
                    chary += 15
            if event.key == K_UP:
                    chary -= 15
        elif CACS == True: 
            charx,chary = 400,300
        elif CATH == True:
            moveRequest = 1004
        elif CAHY == True: 
            moveRequest = 1002
        elif CABB == True:
            moveRequest = 1006             
        else:
            charx, chary = 400,300
        return charx, chary, moveRequest

############## MOVEMENT FOR THAYER HALL #################       
    elif currentArea == THAYER:
        if THarea1 or THarea2 or THarea3 or THarea4 or THarea5 or THarea6 or THarea7 or THarea8 == True:
            if event.key == K_RIGHT:
                charx += 15
            if event.key == K_LEFT:
                charx -= 15
            if event.key == K_DOWN:
                chary += 15
            if event.key == K_UP:
                chary -= 15
        elif THCS == True:
            moveRequest = 4005
        elif THCA == True:
            moveRequest = 4001
        else:
            charx, chary = 400,300
        return charx, chary, moveRequest

############## MOVEMENT FOR MICHIE STADIIUM #############
    elif currentArea == MICHIE:
        if MSarea1 or MSarea2 or MSarea3 == True:
            if event.key == K_RIGHT:
                charx += 15
            if event.key == K_LEFT:
                charx -= 15
            if event.key == K_DOWN:
                chary += 15
            if event.key == K_UP:
                chary -= 15
        elif MSHY == True:
            moveRequest = 3002
        else:
            charx, chary = 400,300
        return charx, chary, moveRequest

############# MOVEMENT FOR HAYES ################
    elif currentArea == HAYES:
        if HAarea1 or HAarea2 or HAarea3 or HAarea4 or HAarea5 or HAarea6 or HAarea7 == True:
            if event.key == K_RIGHT:
                charx += 15
            if event.key == K_LEFT:
                charx -= 15
            if event.key == K_DOWN:
                chary += 15
            if event.key == K_UP:
                chary -= 15
        elif HACA == True:
            moveRequest = 2001
        elif HAMS == True:
            moveRequest = 2003
        else:
            charx, chary = 400,300
        return charx, chary, moveRequest

############# MOVEMENT FOR CADET STORE ###########
    elif currentArea == CSTORE:
        if CSarea1 or CSarea2 or CSarea3 or CSarea4 or CSarea5 or CSarea6 or CSarea7 or CSarea8 or CSarea9 == True:
            if event.key == K_RIGHT:
                charx += 15
            if event.key == K_LEFT:
                charx -= 15
            if event.key == K_DOWN:
                chary += 15
            if event.key == K_UP:
                chary -= 15
        elif CSCA == True:
            moveRequest = 5001
        else:
            charx, chary = 400,300
        return charx, chary, moveRequest
    
        
def startChar(charRect):
    charX= 400
    charY = 300
    charRect.center = (charX, charY)
    
    return charX, charY



def charGetsBelt(charRect, beltRect):
    if charRect.colliderect(beltRect) == True:
        return True
    else:
        return False
        
def charGetsPMI(charRect, PMIRect):
    if charRect.colliderect(PMIRect) == True:
        return True
    else:
        return False

def charGetsHurt(charRect, firstRect):
    if charRect.colliderect(firstRect) == True:
        return True
    else:
        return False
        
def charGetsHW(charRect, HWRect):
    if charRect.colliderect(HWRect) == True:
        return True
    else:
        return False

def charGetsFood(charRect, FoodRect):
    if charRect.colliderect(FoodRect) == True:
        return True
    else:
        return False
        
def charGetsTicket(charRect, ticketRect):
    if charRect.colliderect(ticketRect) == True:
        return True
    else:
        return False

def charGetsCAC(charRect, CACRect):
    if charRect.colliderect(CACRect) == True:
        return True
    else:
        return False        
        
def drawText(text, font, surface, x, y, loc):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()

    if loc == "c":
        textrect.center = (x,y)
    elif loc == "l":
        textrect.topleft = (x,y)
    elif loc == "r":
        textrect.topright = (x,y)        
    surface.blit(textobj, textrect)  
    
'''def displayEnemies(currentState):
    DISPLAYSURF.blit(firstie,firstieRect)
    for num in range(0,6):
        firstX += 10
        firstY += 10
        firstieRect.center = firstX,firstY
        pygame.display.update()
        firstX -= 10
        firstY -= 10
        firstieRect.center = firstX,firstY
        pygame.display.update()    '''      

def terminate():
    pygame.quit()
    sys.exit()

############################################################





        
def playGame():
  pygame.init()
  DISPLAYSURF = pygame.display.set_mode((800, 600))
  pygame.display.set_caption("CDT X's Adventure")
  FPS = 30
  fpsClock = pygame.time.Clock()
  char = pygame.image.load("images/yuk1.gif")
  belt = pygame.image.load("images/Belt.png")
  PMI = pygame.image.load("images/PMI.png")
  CAC = pygame.image.load("images/CAC.png")
  food = pygame.image.load("images/food.png")
  ticket = pygame.image.load("images/ticket.png")
  HW = pygame.image.load("images/hw.png")
  CentralArea = pygame.image.load("images/centralarea.png")
  Thayer = pygame.image.load("images/thayer.png")
  Michie = pygame.image.load("images/michie.png")
  CStore = pygame.image.load("images/cstore.png")
  Hayes = pygame.image.load("images/hayes.png")  
  CharScreen = pygame.image.load("images/charChoose.png")
  StartScreen = pygame.image.load("images/WelcomeScreen.png")
  WinScreen = pygame.image.load("images/WinScreen.png")
  firstie = pygame.image.load("images/firstie1.gif")
  
  charX = 25
  charY = 25
  beltX = 1050
  beltY = 1050
  PMIX = 1050
  PMIY = 1050
  cacX = 1050
  cacY = 1050
  foodX = 1050
  foodY = 1050
  ticketX = 1050
  ticketY = 1050
  HWX = 1050
  HWY = 1050
  firstX = 1050
  firstY = 1050
  squidX = 1050
  squidY = 1050
  HEALTH = 100
  timer = 0
  gotBelt=False
  gotHW=False
  gotCAC=False
  gotPMI = False
  gotfood = False
  gotticket = False
  moveRequest = False  
  font = pygame.font.SysFont(None, 20)
  gameTime = 0
  
 #HW,belt,CAC,PMI,Thayer,Michie,CentralArea,CStore,Hayes,StartScreen = loadCharImages()
  charRect = char.get_rect()
  beltRect = belt.get_rect()
  PMIRect = PMI.get_rect()
  firstieRect = firstie.get_rect()
  PMIRect.center = (PMIX,PMIY)
  charRect.center = (charX, charY)
  beltRect.center = (beltX, beltY)
  firstieRect.center = (firstX,firstY)
  CACRect =CAC.get_rect()
  CACRect.center = (cacX,cacY)
  HWRect = HW.get_rect()
  HWRect.center = (HWX,HWY)
  foodRect = food.get_rect()
  foodRect.center = (foodX,foodY)
  ticketRect = ticket.get_rect()
  ticketRect.center = (ticketX,ticketY)
  currentState = WELCOMESCREEN
 #PMIRect = PMI.get_rect()
 #CACRect =CAC.get_rect()
 #HWRect = HW.get_rect()
  currentState = WELCOMESCREEN
  
  while True:
    if currentState == WELCOMESCREEN:
        HEALTH = 100
        gotBelt = False
        gotPMI = False
        gotticket = False
        gotfood = False
        gotHW = False
        gotCAC = False
        gotPMI = False
        DISPLAYSURF.blit(StartScreen,(0,0))
        for event in pygame.event.get():                
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_RETURN:
                    currentState = CHARSELECT
        pygame.display.update()     
    elif currentState == CHARSELECT:
        DISPLAYSURF.blit(CharScreen,(0,0))
        pygame.display.update()
        for event in pygame.event.get():                
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_1:
                    charSkin = "firstie1.gif"
                    currentState = CAinit
                if event.key == K_2:
                    charSkin = "yuk1.gif"
                    currentState = CAinit                    
                if event.key == K_3:
                    charSkin = "plebe1.gif"
                    currentState = CAinit                   
                if event.key == K_4:
                    charSkin = "cow1.gif"
                    currentState = CAinit 
                if event.key == K_5:
                    charSkin = "football1.gif"
                    currentState = CAinit 
                    
#############################################################################################################
                               
    elif currentState == CAinit:
        char = pygame.image.load("images/{0}".format(charSkin))
        charX,charY = 400,300
        if gotHW == False:
            HWX, HWY = 600,200
        if gotBelt == False:
            betlX, beltY = 1050,1050
        if gotCAC == False:
            CACX, CACY = 1050,1050
        if gotPMI == False:
            PMIX, PMIY = 1050,1050
        if gotticket == False:
            ticketX, ticketY = 1050,1050
        if gotfood == False:
            foodX, foodY = 1050,1050

        firstX, firstY = 580,305
        currentState = CENTRALAREA
        NOTICE = "Welcome to the Area. Find your CAC or "
        NOTICE2 = "you might be spending more time here..."
        startTime = time.time()
        
    elif currentState == CENTRALAREA:
        DISPLAYSURF.blit(char,charRect)
        DISPLAYSURF.blit(belt, beltRect)
        DISPLAYSURF.blit(PMI,PMIRect)
        DISPLAYSURF.blit(CAC,CACRect)
        DISPLAYSURF.blit(food,foodRect)
        DISPLAYSURF.blit(HW,HWRect)
        DISPLAYSURF.blit(ticket,ticketRect)
        DISPLAYSURF.blit(firstie,firstieRect)
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")       
        for event in pygame.event.get():
          if event.type == QUIT:
            pygame.quit()
            sys.exit()
          elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
            charX, charY, moveRequest = moveChar(currentState,charX,charY,event)
            pygame.display.update()
            
        if charGetsHurt(charRect, firstieRect):
            HEALTH -= 1 
        charRect.center = (charX, charY)
        beltRect.center = (beltX,beltY)
        CACRect.center = (cacX,cacY)
        HWRect.center = (HWX,HWY)
        foodRect.center = (foodX,foodY)
        ticketRect.center = (ticketX,ticketY)        
        firstieRect.center = (firstX,firstY)
        DISPLAYSURF.blit(CentralArea,(0,0))
        DISPLAYSURF.blit(char,charRect)
        DISPLAYSURF.blit(belt, beltRect)
        DISPLAYSURF.blit(PMI,PMIRect)
        DISPLAYSURF.blit(CAC,CACRect)
        DISPLAYSURF.blit(food,foodRect)
        DISPLAYSURF.blit(HW,HWRect)
        DISPLAYSURF.blit(ticket,ticketRect)
        DISPLAYSURF.blit(firstie,firstieRect)   
        
        if int(time.time()) % 2 == 0 and firstY > 110:
            firstY -= 10
        elif int(time.time()) % 2 == 0 and firstY < 310:
            firstY += 200

        
             
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")            
        pygame.display.update()   
        if charGetsHW(charRect, HWRect) == True:         
            gotHW = True
            HWX,HWY = 510,440
            NOTICE = "You found your homework..."
            NOTICE2 = "Probably should have turned this in by now..."
            
      ##### MOVEMENT #####
        if moveRequest == 1002:
            if gotBelt == True:
                currentState = HAinit
                endTime = time.time()
                gameTime += endTime - startTime                
                moveRequest = None
            else:
                timer = 1000
                NOTICE = "Find the items before moving on!"
                moveRequest = None
                charX, charY = 400, 300                
        if moveRequest == 1004:
            if gotHW == True:
                currentState = THinit
                endTime = time.time()
                gameTime += endTime - startTime                
                moveRequest = None    
            else:
                timer = 1000
                NOTICE = "Find the items before moving on!"
                moveRequest = None
                charX, charY = 400, 300
        if moveRequest == 1005:
            if gotBelt == True:
                currentState = WELCOMESCREEN
                endTime = time.time()
                gameTime += endTime - startTime                
                moveRequest = None    
            else:
                timer = 1000
                NOTICE = "Find the items before moving on!"
                moveRequest = None
                charX, charY = 400, 300
        if moveRequest == 1006:
            if gotBelt == True:
                currentState = WIN
                endTime = time.time()
                gameTime += endTime - startTime                
                moveRequest = None    
            else:
                timer = 1000
                NOTICE = "Find the items before moving on!"
                moveRequest = None
                charX, charY = 400, 300  
                                      
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")       
        pygame.display.update()
        fpsClock.tick(FPS)
        if HEALTH < 0:
            currentState = WELCOMESCREEN

################## THAYER INIT ###########################################################################
    elif currentState == THinit:
        char = pygame.image.load("images/{0}".format(charSkin))
        charX,charY = 400,150
        if gotBelt == False:
            beltX, beltY = 40,550
        if gotHW == False:
            HWX, HWY = 600,200
        if gotCAC == False:
            CACX, CACY = 1050,1050
        if gotPMI == False:
            PMIX, PMIY = 1050,1050
        if gotticket == False:
            ticketX, ticketY = 1050,1050
        if gotfood == False:
            foodX, foodY = 1050,1050
            
        firstX, firstY = 80,90
        currentState = THAYER
        NOTICE = "You are now in Thayer Hall."
        NOTICE2 = "The smell of chalk and nervous cadets is in the air."

    elif currentState == THAYER:
        DISPLAYSURF.blit(char,charRect)
        DISPLAYSURF.blit(belt, beltRect)
        DISPLAYSURF.blit(PMI,PMIRect)
        DISPLAYSURF.blit(CAC,CACRect)
        DISPLAYSURF.blit(food,foodRect)
        DISPLAYSURF.blit(HW,HWRect)
        DISPLAYSURF.blit(ticket,ticketRect)
        DISPLAYSURF.blit(firstie,firstieRect)
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")       
        for event in pygame.event.get():
          if event.type == QUIT:
            pygame.quit()
            sys.exit()
          elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
            charX, charY, moveRequest = moveChar(currentState,charX,charY,event)
            pygame.display.update()
            
        if charGetsHurt(charRect, firstieRect):
            HEALTH -= 1 
        charRect.center = (charX, charY)
        beltRect.center = (beltX,beltY)
        CACRect.center = (cacX,cacY)
        HWRect.center = (HWX,HWY)
        foodRect.center = (foodX,foodY)
        ticketRect.center = (ticketX,ticketY)        
        firstieRect.center = (firstX,firstY)
        DISPLAYSURF.blit(Thayer,(0,0))
        DISPLAYSURF.blit(char,charRect)
        DISPLAYSURF.blit(belt, beltRect)
        DISPLAYSURF.blit(PMI,PMIRect)
        DISPLAYSURF.blit(CAC,CACRect)
        DISPLAYSURF.blit(food,foodRect)
        DISPLAYSURF.blit(HW,HWRect)
        DISPLAYSURF.blit(ticket,ticketRect)
        DISPLAYSURF.blit(firstie,firstieRect)   
             
        if int(time.time()) % 2 == 0 and firstY > 110:
            firstY -= 10
        elif int(time.time()) % 2 == 0 and firstY < 310:
            firstY += 200

        
             
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")            
        pygame.display.update()
           
        if charGetsBelt(charRect, beltRect) == True:         
            gotBelt = True
            beltX,beltY = 510,400
            NOTICE = "You found a PT Belt"
            NOTICE2 = ""
            
     ##### MOVEMENT #####
        if moveRequest == 4005:
            if gotBelt == True:
                currentState = CSinit
                endTime = time.time()
                gameTime += endTime - startTime                
                moveRequest = False   
            else:
                timer = 1000
                NOTICE = "Find the items before moving on!"
                NOTICE2 = ""
                moveRequest = False
                charX, charY = 400, 300 

        if moveRequest == 4001:
            if gotBelt == True:
                currentState = CAinit
                endTime = time.time()
                gameTime += endTime - startTime                
                moveRequest = False   
            else:
                timer = 1000
                NOTICE = "Find the items before moving on!"
                NOTICE2 = ""
                moveRequest = False
                charX, charY = 400, 300 
                
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")    
        pygame.display.update()
        fpsClock.tick(FPS)
        if HEALTH < 0:
            currentState = WELCOMESCREEN


###############################################################################################################
########### HAYES INIT ###################################################################################################
    elif currentState == HAinit:
        char = pygame.image.load("images/{0}".format(charSkin))
        charX,charY = 400,150
        if gotPMI == False:
            PMIX, PMIY = 40,450
        if gotHW == False:
            HWX, HWY = 1050,1050
        if gotBelt == False:
            betlX, beltY = 1050,1050
        if gotCAC == False:
            CACX, CACY = 1050,1050
        if gotticket == False:
            ticketX, ticketY = 1050,1050
        if gotfood == False:
            foodX, foodY = 1050,1050
        firstX, firstY = 8000,9000
        currentState = HAYES
        NOTICE = "You are now in Hayes Gym."
        NOTICE2 = "Every cadets favorite place."
##############    HAYES    ############################################################################################        
    elif currentState == HAYES:
        DISPLAYSURF.blit(char,charRect)
        DISPLAYSURF.blit(belt, beltRect)
        DISPLAYSURF.blit(PMI,PMIRect)
        DISPLAYSURF.blit(CAC,CACRect)
        DISPLAYSURF.blit(food,foodRect)
        DISPLAYSURF.blit(HW,HWRect)
        DISPLAYSURF.blit(ticket,ticketRect)
        DISPLAYSURF.blit(firstie,firstieRect)
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")       
        for event in pygame.event.get():
          if event.type == QUIT:
            pygame.quit()
            sys.exit()
          elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
            charX, charY, moveRequest = moveChar(currentState,charX,charY,event)
            pygame.display.update()
            
        if charGetsHurt(charRect, firstieRect):
            HEALTH -= 1 
        charRect.center = (charX, charY)
        beltRect.center = (beltX,beltY)
        CACRect.center = (cacX,cacY)
        HWRect.center = (HWX,HWY)
        foodRect.center = (foodX,foodY)
        ticketRect.center = (ticketX,ticketY)        
        firstieRect.center = (firstX,firstY)
        PMIRect.center = (PMIX,PMIY)
        DISPLAYSURF.blit(Hayes,(0,0))
        DISPLAYSURF.blit(char,charRect)
        DISPLAYSURF.blit(belt, beltRect)
        DISPLAYSURF.blit(PMI,PMIRect)
        DISPLAYSURF.blit(CAC,CACRect)
        DISPLAYSURF.blit(food,foodRect)
        DISPLAYSURF.blit(HW,HWRect)
        DISPLAYSURF.blit(ticket,ticketRect)
        DISPLAYSURF.blit(firstie,firstieRect)   
             
#        if int(time.time()) % 2 == 0 and firstY > 110:
#            firstY -= 10
#        elif int(time.time()) % 2 == 0 and firstY < 310:
#            firstY += 200
             
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")            
        pygame.display.update()
           
        if charGetsPMI(charRect, PMIRect) == True:         
            gotPMI = True
            PMIX,PMIY = 540,400
            NOTICE = "You found a PMI slip."
            NOTICE2 = "Too bad you can't use it."
            
     ##### MOVEMENT #####
        if moveRequest == 2001:
            currentState = CAinit
            endTime = time.time()
            gameTime += endTime - startTime                
            moveRequest = None   
        elif moveRequest == 2003:
            if gotticket == True:
                currentState = MSinit 
                endTime = time.time()
                gameTime += endTime - startTime                
                moveRequest = None
                charX, charY = 400, 300
            else:
                timer = 1000
                NOTICE = "Find the items before moving on!"
                NOTICE2 = ""
                moveRequest = None
                charX, charY = 400, 300 
                 
                     
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")       
        pygame.display.update()
        fpsClock.tick(FPS)
        if HEALTH < 0:
            currentState = WELCOMESCREEN
            
################################ CSTORE INIT ############################3
############################################################################

    elif currentState == CSTORE:
        DISPLAYSURF.blit(char,charRect)
        DISPLAYSURF.blit(belt, beltRect)
        DISPLAYSURF.blit(PMI,PMIRect)
        DISPLAYSURF.blit(CAC,CACRect)
        DISPLAYSURF.blit(food,foodRect)
        DISPLAYSURF.blit(HW,HWRect)
        DISPLAYSURF.blit(ticket,ticketRect)
        DISPLAYSURF.blit(firstie,firstieRect)
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")       
        for event in pygame.event.get():
          if event.type == QUIT:
            pygame.quit()
            sys.exit()
          elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
            charX, charY, moveRequest = moveChar(currentState,charX,charY,event)
            pygame.display.update()
            
        if charGetsHurt(charRect, firstieRect):
            HEALTH -= 1 
        charRect.center = (charX, charY)
        beltRect.center = (beltX,beltY)
        CACRect.center = (cacX,cacY)
        HWRect.center = (HWX,HWY)
        foodRect.center = (foodX,foodY)
        ticketRect.center = (ticketX,ticketY)        
        firstieRect.center = (firstX,firstY)
        DISPLAYSURF.blit(CThayer,(0,0))
        DISPLAYSURF.blit(char,charRect)
        DISPLAYSURF.blit(belt, beltRect)
        DISPLAYSURF.blit(PMI,PMIRect)
        DISPLAYSURF.blit(CAC,CACRect)
        DISPLAYSURF.blit(food,foodRect)
        DISPLAYSURF.blit(HW,HWRect)
        DISPLAYSURF.blit(ticket,ticketRect)
        DISPLAYSURF.blit(firstie,firstieRect)   
             
#        if int(time.time()) % 2 == 0 and firstY > 110:
#            firstY -= 10
#        elif int(time.time()) % 2 == 0 and firstY < 310:
#            firstY += 200
             
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")            
        pygame.display.update()
           
        if charGetsfood(charRect, foodRect) == True:         
            gotBelt = True
            beltX,beltY = 580,400
            NOTICE = "You found the last remaining crispitos"
            NOTICE2 = ""
        if charGetsticket(charRect, ticketRect) == True:         
            gotBelt = True
            beltX,beltY = 580,440
            NOTICE = "You found a ticket a football game. Yay."
            NOTICE2 = ""
            
     ##### MOVEMENT #####
        if moveRequest == 5001:
            if gotTicket == True:
                currentState = CAinit
                endTime = time.time()
                gameTime += endTime - startTime                
                moveRequest = False   
            else:
                timer = 1000
                NOTICE = "Find the items before moving on!"
                NOTICE2 = ""
                moveRequest = False
                charX, charY = 400, 300 
                     
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")       
        pygame.display.update()
        fpsClock.tick(FPS)
        if HEALTH < 0:
            currentState = WELCOMESCREEN
##################################################################################################################
###########MICHIE INIT###################################################################################################
    elif currentState == MIinit:
        char = pygame.image.load("images/{0}".format(charSkin))
        charX,charY = 400,150
        if gotCAC == False:
            CACX, CACY = 40,550
#        firstX, firstY = 80,90
        currentState = THAYER
        NOTICE = "You are now in Michie Stadium."
        NOTICE2 = "That was a pretty long walk up here..."
##############    MICHIE    ############################################################################################        
    elif currentState == MICHIE:
        DISPLAYSURF.blit(char,charRect)
        DISPLAYSURF.blit(belt, beltRect)
        DISPLAYSURF.blit(PMI,PMIRect)
        DISPLAYSURF.blit(CAC,CACRect)
        DISPLAYSURF.blit(food,foodRect)
        DISPLAYSURF.blit(HW,HWRect)
        DISPLAYSURF.blit(ticket,ticketRect)
        DISPLAYSURF.blit(firstie,firstieRect)
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")       
        for event in pygame.event.get():
          if event.type == QUIT:
            pygame.quit()
            sys.exit()
          elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
            charX, charY, moveRequest = moveChar(currentState,charX,charY,event)
            pygame.display.update()
            
        if charGetsHurt(charRect, firstieRect):
            HEALTH -= 1 
        charRect.center = (charX, charY)
        beltRect.center = (beltX,beltY)
        CACRect.center = (cacX,cacY)
        HWRect.center = (HWX,HWY)
        foodRect.center = (foodX,foodY)
        ticketRect.center = (ticketX,ticketY)        
        firstieRect.center = (firstX,firstY)
        DISPLAYSURF.blit(CThayer,(0,0))
        DISPLAYSURF.blit(char,charRect)
        DISPLAYSURF.blit(belt, beltRect)
        DISPLAYSURF.blit(PMI,PMIRect)
        DISPLAYSURF.blit(CAC,CACRect)
        DISPLAYSURF.blit(food,foodRect)
        DISPLAYSURF.blit(HW,HWRect)
        DISPLAYSURF.blit(ticket,ticketRect)
        DISPLAYSURF.blit(firstie,firstieRect)   
             
#        if int(time.time()) % 2 == 0 and firstY > 110:
#            firstY -= 10
#        elif int(time.time()) % 2 == 0 and firstY < 310:
#            firstY += 200
             
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")            
        pygame.display.update()
           
        if charGetsCAC(charRect, CACRect) == True:         
            gotCAC = True
            CACX,CACY = 540,440
            NOTICE = "You finally found your CAC!"
            NOTICE2 = "Now lets get back to your room."

            
     ##### MOVEMENT #####
        if moveRequest == 3002:
            if gotCAC == True:
                currentState = HAinit
                endTime = time.time()
                gameTime += endTime - startTime                
                moveRequest = None   
            else:
                timer = 1000
                NOTICE = "Find the items before moving on!"
                NOTICE2 = ""
                moveRequest = False
                charX, charY = 400, 300 
                     
        drawText("INVENTORY", font, DISPLAYSURF, 640, 375, "c")
        drawText("HEALTH: {0}".format(HEALTH), font, DISPLAYSURF, 640, 535, "c")
        drawText("NOTICE: {0}".format(NOTICE), font, DISPLAYSURF, 640, 560, "c")
        drawText("{0}".format(NOTICE2), font, DISPLAYSURF, 640, 575, "c")         
        drawText("TIME: {0}".format(int(time.time()-startTime)), font, DISPLAYSURF, 640, 520, "c")       
        pygame.display.update()
        fpsClock.tick(FPS)
        if HEALTH < 0:
            currentState = WELCOMESCREEN

##################################################################################################################


    elif currentState == WIN:
        HEALTH = 100
        gotBelt = False
        DISPLAYSURF.blit(WinScreen,(0,0))
        drawText("{0}".format(int(gameTime)), font, DISPLAYSURF, 350, 128, "c")
        pygame.display.update()
        drawText("{0}".format(int(gameTime)), font, DISPLAYSURF, 350, 128, "c")        
        pygame.display.update()        
        drawText("{0}".format(int(gameTime)), font, DISPLAYSURF, 350, 128, "c")        
        drawText("{0}".format(int(gameTime)), font, DISPLAYSURF, 350, 128, "c")        
        drawText("{0}".format(int(gameTime)), font, DISPLAYSURF, 350, 128, "c")                
        for event in pygame.event.get():                
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_RETURN:
                    currentState = CHARSELECT
        
        
  
'''  
    DISPLAYSURF.blit(char,(charX,charY))
    DISPLAYSURF.fill(BLUE)
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            terminate()
        charX, charY = moveChar(charX,charY,event)
      elif event.type == MOUSEMOTION:
        charX = event.pos[0]
        charY = event.pos[1]
    DISPLAYSURF.blit(char,(charX,charY))
    pygame.display.update()
    fpsClock.tick(FPS)
'''









############################################################


    
        

if __name__ == "__main__":
  playGame()
