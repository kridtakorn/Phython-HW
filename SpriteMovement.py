import pygame  as game

WIDTH = 600
HEIGHT = 500
FPS =60

RED = (255,0,0)
BLACK =(0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Player1(game.sprite.Sprite):
    def __init__(self):
        game.sprite.Sprite.__init__(self)
        self.image = game.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)

    def update(self):
        self.rect.y += 5
        if self.rect.top>HEIGHT:
            self.rect.top = 0

class Player2(game.sprite.Sprite):
    def __init__(self):
        game.sprite.Sprite.__init__(self)
        self.image = game.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)

    def update(self):
        self.rect.y -= 5
        if self.rect.top<0:
            self.rect.top = HEIGHT
        

        
            
            



game.init()
game.mixer.init()
screen = game.display.set_mode((WIDTH,HEIGHT))
game.display.set_caption("6006597 Game")
clock = game.time.Clock()

all_sprites = game.sprite.Group()
Character1 = Player1()
Character2 = Player2()
all_sprites.add(Character1)
all_sprites.add(Character2)

running = True
while running:
    clock.tick(FPS)
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    all_sprites.update()
    
    screen.fill(BLUE)
    all_sprites.draw(screen)
    game.display.flip()
game.quit()   