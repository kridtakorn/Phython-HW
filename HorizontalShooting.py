import pygame  as game
import random

WIDTH = 600
HEIGHT = 500
FPS =60

RED = (255,0,0)
BLACK =(0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Character(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game.Surface((50,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.left = 20
        self.rect.bottom = HEIGHT-10
        self.speedy = 0
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):
         bullet = Bullet(self.rect.right,self.rect.centery)
         all_sprites.add(bullet)
         bullets.add(bullet)

class Mob(game.sprite.Sprite):
    def __init__(self):
        game.sprite.Sprite.__init__(self)
        self.image = game.Surface((40,30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.rect.x = random.randrange(WIDTH + 40, WIDTH + 100)
        self.speedx = random.randrange(-8 , -1)
        self.speedy = random.randrange(-3 , 3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left < 0:
            self.rect.y = random.randrange(HEIGHT-self.rect.height)
            self.rect.x = random.randrange(WIDTH + 40, WIDTH + 100)
            self.speedx = random.randrange(-8 , -1)
        

class Bullet(game.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = game.Surface((20,10))
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.centery = y
        self.speedx =-10
        self.speedy =-10 

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < WIDTH :
            self.kill
       

        

game.init()
game.mixer.init()
screen = game.display.set_mode((WIDTH,HEIGHT))
game.display.set_caption("6006597 Game")
clock = game.time.Clock()

all_sprites = game.sprite.Group()
mobs = game.sprite.Group()
bullets = game.sprite.Group()

character = Character()
all_sprites.add(character)

for i in range(20):
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)

running = True
while running:
    clock.tick(FPS)
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

        if event.type == game.KEYUP:
            if event.key == game.K_w:
                character.speedy = 0
            if event.key == game.K_s:
                character.speedy = 0
        if event.type == game.KEYDOWN:
            if event.key == game.K_w:
                character.speedy = -5
            if event.key == game.K_s:
                character.speedy = 5
            if event.key == game.K_SPACE:
                character.shoot()      
        



    all_sprites.update()
    Death = game.sprite.spritecollide(character,mobs,False)
    if Death:
        running = False
    Die = game.sprite.groupcollide(mobs,bullets,True,True)
    for hit in Die:
        d = Mob()
        all_sprites.add(d)
        mobs.add(d)

    screen.fill(BLUE)
    
    all_sprites.draw(screen)
    game.display.flip()
game.quit()   