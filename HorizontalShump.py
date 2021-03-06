import pygame  as game

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
       

        

game.init()
game.mixer.init()
screen = game.display.set_mode((WIDTH,HEIGHT))
game.display.set_caption("6006597 Game")
clock = game.time.Clock()

all_sprites = game.sprite.Group()

character = Character()
all_sprites.add(character)

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
        



    all_sprites.update()    
    screen.fill(BLUE)
    all_sprites.draw(screen)
    game.display.flip()
game.quit()   