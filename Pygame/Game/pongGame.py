import pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.init()

#Initializing the display window 

size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#Starting co-ordinates of the paddle

rectX = 400
rectY = 580

#initial speed of the paddle 

rectChangeX = 0
rectChangeY = 0

#initial positionn of the ball

ballX = 50
ballY = 50

#speed of the ball

ballChangeX = 5
ballChangeY = 5

score = 0

#draws the paddle 
def drawRect(screen,x,y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699
    pygame.draw.rect(screen,red,[x,y,100,20])

#game loop

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rectChangeX = -6
            elif event.key == pygame.K_RIGHT:
                rectChangeX = 6
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rectChangeX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rectChangeY = 0
        screen.fill(black)
        rectX += rectChangeX
        rectY += rectChangeY

        ballX += ballChangeX
        ballY += ballChangeY

        #this handles the movement of the ball
        if ballX < 0:
            ballX = 0
            ballChangeX = ballChangeX * -1
        elif ballX > 785:
            ballX = 785
            ballChangeX = ballChangeX * -1
        elif ballX > rectX and ballX < rectX + 100 and ballY == 565:
            score += 1
        elif ballY > 600:
            ballChangeY = ballChangeY * -1
            score = 0
        pygame.draw.rect(screen,white,[ballX,ballY,15,15])

        #drawing ball
        drawRect(screen,rectX,rectY)

        #score board
        font = pygame.font.SysFont('Calibri',15,False,False)
        text = font.render("Score = "+str(score),True,white)
        screen.blit(text,[600,100])

        pygame.display.flip()
        clock.tick(60)
pygame.quit()
