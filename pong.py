import pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('ArcadeClassic',50)
size = (800,600)
screen = pygame.display.set_mode(size)
screen_rect = screen.get_rect()
pygame.display.set_caption("Pong")

tick = pygame.time.Clock()

player1points = 0
player2points = 0
run = True
playergroup = pygame.sprite.Group()
class player(pygame.sprite.Sprite):
    def __init__(self, no):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25,100])
        self.image.fill((255,255,255))
        self.playery = 250
        self.rect = self.image.get_rect()
        self.no = no
        if no == 1:
            self.rect = pygame.Rect(25, self.playery, 25, 100)
        elif no == 2:
            self.rect = pygame.Rect(750, self.playery, 25, 100)
    def update(self):
        if self.no == 1:
            self.rect = pygame.Rect(25, self.playery, 25, 100)
        elif self.no == 2:
            self.rect = pygame.Rect(750, self.playery, 25, 100)
    def checkcollision(self):
        col = pygame.sprite.collide_rect(self, ball)
        if col:
            ball.velx = -ball.velx
            ball.vely = ((ball.posy+12.5) - (self.playery+50))*0.05   
            if ball.velx < 0:
                ball.velx -= 0.5
            else:
                ball.velx += 0.5
ballgroup = pygame.sprite.Group()
class ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25,25])
        self.image.fill((255,255,255))
        self.posx = 387.5
        self.posy = 287.5
        self.velx = -2
        self.vely= 0
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.posx, self.posy, 25, 25)
    def update(self):
        self.posx += self.velx
        self.posy += self.vely
        self.rect = pygame.Rect(self.posx, self.posy, 25, 25)
ball = ball()        
player1 = player(1)
player2 = player(2)
ballgroup.add(ball)
playergroup.add(player1)
playergroup.add(player2)
    
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    move_ticker = 0
    move_ticker2 = 0
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and keys[pygame.K_s]:
        if move_ticker == 0:
            move_ticker = 10
    elif keys[pygame.K_s]:
        if move_ticker == 0:
            move_ticker = 10
            player1.playery += 5
    elif keys[pygame.K_w]:
        if move_ticker == 0:
            move_ticker = 10
            player1.playery -= 5

    if keys[pygame.K_DOWN] and keys[pygame.K_UP]:
        if move_ticker2 == 0:
            move_ticker2 = 10
    elif keys[pygame.K_DOWN]:
        if move_ticker2 == 0:
            move_ticker2 = 10
            player2.playery += 5
    elif keys[pygame.K_UP]:
        if move_ticker2 == 0:
            move_ticker2 = 10
            player2.playery -= 5

    screen.fill((0,0,0))

    player1.checkcollision()
    player2.checkcollision()

    if 0 >= ball.posy:
        ball.vely = -ball.vely
    if ball.posy > 587.5:
        ball.vely = -ball.vely

    if 0 >= ball.posx:
        ball.posx = 387.5
        ball.posy = 287.5
        ball.velx = 2
        ball.vely = 0
        player2points += 1
    if ball.posx >= 775:
        ball.posx = 387.5
        ball.posy = 287.5
        ball.velx = -2
        ball.vely = 0
        player1points += 1

    if ball.velx > 45:
        ball.velx = 45
    elif ball.velx < -45:
        ball.velx = -45
    
    if player1.playery < 0:
        player1.playery = 0
    if player1.playery > 500:
        player1.playery = 500
    if player2.playery < 0:
        player2.playery = 0
    if player2.playery > 500:
        player2.playery = 500
    
    if keys[pygame.K_SPACE]:
        ball.posx = 850
        player1points = -1
        player2points = 0

    pygame.draw.rect(screen, (255,255,255), [399,0,2,64])
    pygame.draw.rect(screen, (255,255,255), [399,133,2,64])
    pygame.draw.rect(screen, (255,255,255), [399,266,2,64])
    pygame.draw.rect(screen, (255,255,255), [399,400,2,64])
    pygame.draw.rect(screen, (255,255,255), [399,534,2,64])

    textsurface = myfont.render(str(player1points), False, (255, 255, 255))
    textsurface2 = myfont.render(str(player2points), False, (255, 255, 255))
    if player1points < 0:
            textsurface = myfont.render('0', False, (255, 255, 255))
    if player2points < 0:
            textsurface2 = myfont.render('0', False, (255, 255, 255))

    screen.blit(textsurface,(335,10))
    screen.blit(textsurface2,(435,10))
    
    playergroup.update()
    ball.update()
    playergroup.draw(screen)
    ballgroup.draw(screen)
    pygame.display.flip()
    if move_ticker > 0:
        move_ticker -= 1
    if move_ticker2 > 0:
        move_ticker2 -= 1
    tick.tick(60)

pygame.quit()
