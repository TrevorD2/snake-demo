import pygame as pg
import random
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

  def gen_apple(self):
    new_state = 1
    while new_state != 0:
      apple_x = random.randint(0, self.width-1)
      apple_y = random.randint(0, self.height-1)

      new_state = self.matrix[apple_x][apple_y].state
    
    self.matrix[apple_x][apple_y].switch_state(1)

class Snake():
  def __init__(self, grid):
    self.grid = grid

    self.body = [(0, 0), (1, 0), (2, 0)]
    self.length = len(self.body)
    for (x, y) in self.body:
      self.grid.matrix[x][y].switch_state(2)

    self.dir = (1, 0)

  def move(self):
    nx, ny = self.body[-1]
    nx += self.dir[0]
    ny += self.dir[1]

    nx, ny = nx % self.grid.width, ny % self.grid.height

    if self.grid.matrix[nx][ny].state == 1:
      self.grid.gen_apple()
    else:
      tail_x, tail_y = self.body[0]
      self.grid.matrix[tail_x][tail_y].switch_state(0)
      self.body.pop(0)

    self.grid.matrix[nx][ny].switch_state(2)
    self.body.append((nx, ny))



grid = Grid(25, 25)
snake = Snake(grid)
grid.gen_apple()

#Vars
clock = pg.time.Clock()
running = True
start_moving = False

while running:
  #Limits fps to 3
  clock.tick(3)

  up, down, left, right = False, False, False, False

  #Exits on game quit (close tab)
  for event in pg.event.get():
    if event.type == pg.QUIT: 
      running = False

    if event.type == pg.KEYDOWN:
      if event.key == pg.K_UP or event.key == pg.K_w:
        up = True
      if event.key == pg.K_DOWN or event.key == pg.K_s:
        down = True
      if event.key == pg.K_LEFT or event.key == pg.K_a:
        left = True
      if event.key == pg.K_RIGHT or event.key == pg.K_d:
        right = True

  if up or down or left or right:
    start_moving = True

  if up and snake.dir != (0, 1):
    snake.dir = (0, -1)
  elif down and snake.dir != (0, -1):
    snake.dir = (0, 1)
  elif left and snake.dir != (1, 0):
    snake.dir = (-1, 0)
  elif right and snake.dir != (-1, 0):
    snake.dir = (1, 0)

  if start_moving:
    snake.move()


  #BG
  screen.fill((255, 255, 255))
  #Objects
  objects.draw(screen)
  #Load
  pg.display.update()