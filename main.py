import pygame as pg
from constants import *
from sprites import *
import random


class Game:
    def __init__(self):
        # Initializes pygame and etc
        pg.init()
        pg.mixer.init()
        pg.display.set_caption('Game')
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True

    def new(self):
        # Starts a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORMS:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.run()

    def run(self):
        # Main game loop
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                    #print(pg.mouse.get_pos())

    def update(self):
        # Game loop - update
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        # Scroll up
        if self.player.rect.top < round((HEIGHT / 3) * 0.5):
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += int(abs(self.player.vel.y))
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    # sprite.kill()
                    self.running = False
                    self.playing = False

        # Spawn new platforms after scroll
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-80, -50),
                         width, 20)
            self.all_sprites.add(p)
            self.platforms.add(p)

    def draw(self):
        # Game loop - draw
        self.window.fill(BLACK)
        bg_img = pg.image.load('bg.png')
        self.window.blit(bg_img, (0, 0))

        self.all_sprites.draw(self.window)
        pg.display.flip()


g = Game()
while g.running:
    g.new()
pg.quit()
