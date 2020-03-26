import pygame,sys
import time
import random

pygame.init()

white = (255,255,255)
black = (100,0,0)
red = (255,0,0)
windowHeight = 600
windowWidth = 800

gameDisplay = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
FPS = 60
blockSize = 20
noPixel = 0

def myQuit():
    pygame.quit()
    sys.exit(0)

font = pygame.font.SysFont(None,25,bold = True)

def drawGrid():
    gridSize = windowWidth // blockSize

def snake(blockSize,snakelist):
    for size in snakelist:
        pygame.draw.rect(gameDisplay,black,[size[0]+5,size[1],blockSize,blockSize],2)

def messageToScreen(msg,color):
    screenText = font.render(msg,True,color)
    gameDisplay.blit(screenText,[windowWidth/2,windowHeight/2])

def gameLoop():

    gameExit = False
    gameOver = False

    leadX = windowWidth/2
    leadY = windowHeight/2

    changePixelsOfX = 0
    changePixelsOfY = 0

    snakeList = []
    snakeLength = 1

    randomAppleX = round(random.randrange(0,windowWidth - blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(0,windowHeight - blockSize)/10.0)*10.0

    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            messageToScreen("Game over !! Press 'c' to play again (or) Q to quit",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    if event.key == pygame.K_c:
                        gameLoop()

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myQuit()
                    
                left = event.key == pygame.K_LEFT
                left = event.key == pygame.K_a

                right = event.key == pygame.K_RIGHT
                right = event.key == pygame.K_d

                up = event.key == pygame.K_UP
                up = event.key == pygame.K_w

                down = event.key == pygame.K_DOWN
                down = event.key == pygame.K_s

                if left:
                    changePixelsOfX = -blockSize
                    changePixelsOfY = noPixel
                elif right:
                    changePixelsOfX = blockSize
                    changePixelsOfY = noPixel
                elif up:
                    changePixelsOfY = -blockSize
                    changePixelsOfX = noPixel
                elif down:
                    changePixelsOfY = blockSize
                    changePixelsOfX = noPixel

            if leadX >= windowWidth or leadX < 0 or leadY < 0 or leadY >= windowHeight:
                gameOver = True
                
            leadX += changePixelsOfX
            leadY += changePixelsOfY

            gameDisplay.fill(white)

            appleThickness = 20

            print([int(randomAppleX),int(randomAppleY),appleThickness,appleThickness])
            pygame.draw.rect(gameDisplay,red,[randomAppleX,randomAppleY,appleThickness,appleThickness])

            allSpriteList = []
            allSpriteList.append(leadX)
            allSpriteList.append(leadY)
            snakeList.append(allSpriteList)

            if len(snakeList) > snakeLength:
                del snakeList[0]
                
            for eachSegment in snakeList[:-1]:
                if eachSegment == allSpriteList:
                    gameOver = True

            snake(blockSize,snakeList)

            pygame.display.update()

            if leadX >= randomAppleX and leadX <= randomAppleX + appleThickness:
                if leadY >= randomAppleY and leadY <= randomAppleY + appleThickness:
                    randomAppleX = round(random.randrange(0,windowWidth - blockSize)/10.0)*10.0
                    randomAppleY = round(random.randrange(0,windowHeight - blockSize)/10.0)*10.0
                    snakeLength += 1
                
        clock.tick(FPS)
    pygame.quit()
    quit()


gameLoop()               
