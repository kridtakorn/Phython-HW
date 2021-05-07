import pygame  as game
import random
from os import path

WIDTH = 600
HEIGHT = 500
FPS =60

RED = (255,0,0)
BLACK =(0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__),'snd')



class Character(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game.transform.scale(player_img,(20,20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25
        self.rect.centerx = WIDTH/2
        self.rect.left = 20
        self.rect.bottom = HEIGHT-50
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
         bullet = Bullet(self.rect.centerx,self.rect.top)
         all_sprites.add(bullet)
         bullets.add(bullet)
         ATK_sound.play()

class Mob(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_orig = random.choice(enemy_imgs)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width/2)
        self.rect.x = random.randrange(HEIGHT - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1 , 3)
        self.speedx = random.randrange(-3 , 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8,8)
        self.lastupdate = game.time.get_ticks()
    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT+10:
            self.rect.x = random.randrange(HEIGHT-self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1 , 3)
    def rotate(self):
        now = game.time.get_ticks()
        if now - self.lastupdate > 50:
            self.lastupdate = now
            self.rot = (self.rot + self.rot_speed)%360
            new_image = game.transform.rotate(self.image_orig , self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        

class Bullet(game.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = game.transform.scale(bullet_img,(10,10))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = -10
        self.speedy = -10 

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0 :
            self.kill
       

        

game.init()
game.mixer.init()
screen = game.display.set_mode((WIDTH,HEIGHT))
game.display.set_caption("6006597 Game")
clock = game.time.Clock()

background = game.image.load(path.join(img_dir , 'background.png')).convert()
background_rect = background.get_rect()

expl_sound = []
for snd in ['Explosion.wav' , 'Explosion2.wav']:
    get_sounds = game.mixer.Sound(path.join(snd_dir , snd))
    get_sounds.set_volume(0.4)
    expl_sound.append(get_sounds)

ATK_sound = game.mixer.Sound(path.join(snd_dir,'ATK.mp3'))
game.mixer.music.load(path.join(snd_dir, 'BG.mp3'))
game.mixer.music.set_volume(0.5)

player_img = game.image.load(path.join(img_dir , 'player.png')).convert()

enemy_imgs =[]
enemy_list =['enemy.png','enemy2.png','enemy3.png']
for img in enemy_list:
    enemy_imgs.append(game.image.load(path.join(img_dir, img)).convert()) 


bullet_img = game.image.load(path.join(img_dir , 'fire.png')).convert()

all_sprites = game.sprite.Group()
mobs = game.sprite.Group()
bullets = game.sprite.Group()

character = Character()
all_sprites.add(character)

for i in range(20):
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)

score = 0 

font_name = game.font.match_font('arial')
def draw_text(surf , text , size , x , y):
    font = game.font.Font(font_name , size)
    text_surface = font.render(text , True , BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface , text_rect)

game.mixer.music.play(loops=-1)

running = True
while running:
    clock.tick(FPS)
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

        if event.type == game.KEYUP:
            if event.key == game.K_a:
                character.speedx = 0
            if event.key == game.K_d:
                character.speedx = 0
        if event.type == game.KEYDOWN:
            if event.key == game.K_a:
                character.speedx = -5
            if event.key == game.K_d:
                character.speedx = 5
            if event.key == game.K_SPACE:
                character.shoot()      
        



    all_sprites.update()
    Death = game.sprite.spritecollide(character,mobs,False)
    if Death:
        running = False
    Die = game.sprite.groupcollide(mobs,bullets,True,True)
    for hit in Die:
        score += 10
        random.choice(expl_sound).play()
        d = Mob()
        all_sprites.add(d)
        mobs.add(d)

    screen.fill(BLUE)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score),30,550,450)
    game.display.flip()
game.quit()   