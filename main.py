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
    #0 - empty, 1 - apple, 2 - snake
    self.states = {
      0: Object(size, "grey", pos, True),
      1: Object(size, "red", pos),
      2: Object(size, "green", pos)
    }

    self.state = 0

  def switch_state(self, new_state):
    objects.remove(self.states[self.state])
    self.state = new_state
    objects.add(self.states[self.state])

class Grid():
  def __init__(self, grid_width, grid_height):
    self.width = grid_width
    self.height = grid_height

    self.matrix = []

    for x in range(self.width):
      column = []
      for y in range(self.height):
        rect_size = width/self.width, height/self.height
        rect_pos = x * rect_size[0], y * rect_size[1]
        column.append(Block(rect_size, rect_pos))

      self.matrix.append(column)

class Snake():
  pass

grid = Grid(25, 25)
grid.matrix[10][10].switch_state(2)
#block = Block((50, 50), (0, 0))
#block.switch_state(2)

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