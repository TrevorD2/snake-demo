import pygame as pg
pg.init()

width, height = 500, 500

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Pygame Template")

objects = pg.sprite.Group()

class Object(pg.sprite.Sprite):
  def __init__(self, size, color, pos, in_group = False):
    super().__init__()
    if in_group:
      objects.add(self)

    self.image = pg.Surface(size)
    self.image.fill(color)

    self.rect = self.image.get_rect()
    self.rect.topleft = pos

class Block():
  def __init__(self, size, pos):
    #0 - empty, 1 - snake, 1 - apple
    self.states = {
      0: Object(size, "grey", pos, True),
      1: Object(size, "red", pos),
      2: Object(size, "green", pos)
    }

    self.state = 0

Block((50, 50), (0, 0))

#Vars
clock = pg.time.Clock()
running = True

while running:
  #Limits fps to 30
  clock.tick(30)

  #Exits on game quit (close tab)
  for event in pg.event.get():
    if event.type == pg.QUIT: 
      running = False

  
  #BG
  screen.fill((255, 255, 255))
  #Objects
  objects.draw(screen)
  #Load
  pg.display.update()