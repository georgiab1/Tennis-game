import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1000, 650))
clock = pygame.time.Clock()
running = True
dt = 0
font20 = pygame.font.Font('freesansbold.ttf', 20)
p1Score = 0
p2Score = 0
player = pygame.Rect((100, 300, 50, 50))
player2 = pygame.Rect((825, 300, 50, 50))
scoreBoard = pygame.Rect((414, 5, 102, 60))
walkCount = 0
walkCount2 = 0
ballSleep = 0
Gwalk = [pygame.image.load('Ge2.png'),pygame.image.load('Ge1.png'),pygame.image.load('Ge2.png'),pygame.image.load('Ge3.png')]
Fwalk = [pygame.image.load('Fe2.png'),pygame.image.load('Fe1.png'),pygame.image.load('Fe2.png'),pygame.image.load('Fe3.png')]
bg = pygame.image.load('bg.png')
Sboard = pygame.image.load('scoreboard2.png')
P1Scores = [pygame.image.load('p10.png'),pygame.image.load('p11.png'),pygame.image.load('p12.png'),pygame.image.load('p13.png'),pygame.image.load('p14.png'),pygame.image.load('p15.png'),pygame.image.load('p16.png'),pygame.image.load('p1win.png')]
P2Scores = [pygame.image.load('p20.png'),pygame.image.load('p21.png'),pygame.image.load('p22.png'),pygame.image.load('p23.png'),pygame.image.load('p24.png'),pygame.image.load('p25.png'),pygame.image.load('p26.png'),pygame.image.load('p2win.png')]
class ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
    def display(self):
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
    def update(self):
        global ballSleep
        if ballSleep>150:
            self.posx += self.speed*self.xFac
            self.posy += self.speed*self.yFac
     
            if self.posy <= 100 or self.posy >= 600:
                self.yFac *= -1
     
            if self.posx <= 0 and self.firstTime:
                self.firstTime = 0
                return 1
            elif self.posx >= 1000 and self.firstTime:
                self.firstTime = 0
                return -1
            
            else:
                return 0
     
    def reset(self):
        global ballSleep
        self.posx = 500
        self.posy = 300
        self.xFac *= -1
        self.firstTime = 1
        ballSleep = 0
        
        
        
 
    def hit(self):
        self.xFac *= -1
 
    def getRect(self):
        return self.ball


def redrawGW():
    global walkCount
    global walkCount2
    global p1Score
    global p2Score
    global ballSleep
    ballSleep+=1
    screen.fill("white")
    screen.blit(bg, (0,0))
    if walkCount+1>=16:
        walkCount = 0
    if walkCount2+1>=16:
        walkCount2 = 0
    screen.blit(Fwalk[walkCount//6], player)
    walkCount+=1
    screen.blit(Gwalk[walkCount2//6], player2)
    walkCount2+=1
    screen.blit(Sboard, scoreBoard)
    screen.blit(P1Scores[p1Score], scoreBoard)
    screen.blit(P2Scores[p2Score], scoreBoard)
    Ball.display()
    pygame.display.update()
    
Ball = ball(500, 300, 7, 6, "green")
x = True
while running and x ==True:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.Rect.colliderect(Ball.getRect(), player):
        Ball.hit()
    if pygame.Rect.colliderect(Ball.getRect(), player2):
        Ball.hit()        
                                  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.top>50:
        player.move_ip(0,-300 * dt)
    elif keys[pygame.K_s] and player.bottom<600:
        player.move_ip(0,300 * dt)
    else:
        walkCount=0
                
        
    if keys[pygame.K_UP] and player2.top>50:
        player2.move_ip(0,-300 * dt)
    elif keys[pygame.K_DOWN] and player2.bottom<600:
        player2.move_ip(0,300 * dt)
    else:
        walkCount2 = 0
    dt = clock.tick(60) / 1000
    

    point = Ball.update()
    if point == -1:
        p1Score += 1
    elif point == 1:
        p2Score+=1
        
    if point:   
        Ball.reset()
        ballSleep = 0
    redrawGW()
    if p1Score == 7 or p2Score== 7:
        x = False
if x == False:
    if p1Score>p2Score:
        bg = pygame.image.load('bluewin.png')
    elif p1Score<p2Score:
        bg = pygame.image.load('redwin.png')
while running:
    redrawGW()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.top>50:
        player.move_ip(0,-300 * dt)
    elif keys[pygame.K_s] and player.bottom<600:
        player.move_ip(0,300 * dt)
    else:
        walkCount=0

    if keys[pygame.K_UP] and player2.top>50:
        player2.move_ip(0,-300 * dt)
    elif keys[pygame.K_DOWN] and player2.bottom<600:
        player2.move_ip(0,300 * dt)
    else:
        walkCount2 = 0
    dt = clock.tick(60) / 1000
    
pygame.quit()
