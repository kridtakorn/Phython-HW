import pygame  as game

WIDTH = 600
HEIGHT = 500
FPS =30

RED = (255,0,0)
BLACK =(0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
game.init()
game.mixer.init()
screen = game.display.set_mode((WIDTH,HEIGHT))
game.display.set_caption("6006597 Game")
clock = game.time.Clock()

all_sprites = game.sprite.Group()

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