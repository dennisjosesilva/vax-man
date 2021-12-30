from vaxman_game.Virus import Virus
from vaxman_game.graph.LevelGraph import LevelGraph

import pygame

class Level:

  NEIGHBOUR_OFFSET = [(0,-1), (-1,0), (0,1), (1,0)]

  def __init__(self, filename="levels/test.txt"):
    self.all_tiles = pygame.sprite.Group()
    self.wall_tiles = pygame.sprite.Group()
    self.person_tiles = pygame.sprite.Group()
    self.viruses = pygame.sprite.Group()
    self.player_pos = None 

    with open(filename) as f:
      lines = [l.split() for l in f.readlines()]
      self.graph = LevelGraph(lines)
      self.parseLevel(lines)

  def parseCell(self, lines, row, col):
    t = None 
    if lines[row][col] == "0":
      t = TilePerson(pos=(col*20, row*20))
      self.all_tiles.add(t)
      self.person_tiles.add(t)
    elif lines[row][col] == "1":
      t = self.parseWallTile(lines, row, col)
      self.wall_tiles.add(t)
      self.all_tiles.add(t)
    elif lines[row][col] == "p":
      self.player_pos = (col*20, row*20)
    elif lines[row][col] == "v":
      self.viruses.add(Virus(self, init_pos=(col*20, row*20), level_pos=(row, col)))
      
  def is_in_the_bounds_of_the_level(self, p):
    return 0 <= p[0] and p[0] < self.height and 0 <= p[1] and p[1] < self.width

  def parseWallTile(self, lines, row, col):    
    pattern = ""
    for n in self.NEIGHBOUR_OFFSET:
      q = ( row + n[0], col + n[1] )      
      if self.is_in_the_bounds_of_the_level(q) and lines[q[0]][q[1]] == "1":
        pattern += "1"
      else:
        pattern += "0"
    
    return TileWall(pattern=pattern, pos=(20*col, 20*row))

  def parseLevel(self, lines):
    self.width = len(lines[0])
    self.height = len(lines)

    for row in range(self.height):
      for col in range(self.width):
        self.parseCell(lines, row, col)
  
  def update(self):
    self.viruses.update()

  def draw(self, screen):
    for t in self.all_tiles:
      screen.blit(t.surf, t.rect)

    for v in self.viruses:
      screen.blit(v.surf, v.rect)

  def __str__(self):
    s = ""    
    for t in self.all_tiles:
      s += "\n" + str(t)
    return s

  def number_of_virus(self):
    return len(self.viruses)

  def number_of_unvaccinated_people(self):
    return len(self.person_tiles)

# TILES
# -----
class Tile(pygame.sprite.Sprite):
  def __init__(self):
    super(Tile, self).__init__()
    self.surf = None 
    self.rect = None 

  def draw(self, level):
    level.blit(self.surf, self.rect)

# TILE COLECTABLE (PERSON TO BE VACINED)
# ---------------------------------------
class TilePerson(Tile):
  def __init__(self, pos=(0,0)):
    super(TilePerson, self).__init__()
    self.surf = pygame.Surface((20, 20))
    self.draw_face()
    self.rect = self.surf.get_rect()
    self.rect.move_ip(pos)    

  def draw_face(self):
    # head
    pygame.draw.circle(self.surf, 
      color=(238,232,170),
      center=(10, 10),
      radius=5)

    # left eye
    pygame.draw.circle(self.surf, 
      color=(0,0,0),
      center=(8, 8),
      radius=1)
    
    # right eye
    pygame.draw.circle(self.surf, 
      color=(0,0,0),
      center=(12, 8),
      radius=1)

    pygame.draw.line(self.surf,
      color=(0, 0, 0),
      start_pos=(8, 12), end_pos=(12,12))

  def __str__(self) -> str:
      return "Person"

# TILE WITH WALLS 
# ---------------
class TileWall(Tile):
  
  WALL_COLOR = (255, 0, 0)

  def __init__(self, pattern="0000", pos=(20,20)):
    super(TileWall, self).__init__()
    self.createSurface(pattern)
    self.rect = self.surf.get_rect()
    self.rect.move_ip(pos)

  def createSurface(self, pattern):
    self.surf = pygame.Surface((20, 20))
    self.surf.fill((0,0,0))
    self.pattern = pattern
    if pattern == "0000":
      pygame.draw.lines(self.surf, color=self.WALL_COLOR, closed=True,
        points=[(0,0), (20,0), (20,20), (0,20)], width=10)
    elif pattern == "0001":
      pygame.draw.lines(self.surf, color=self.WALL_COLOR, closed=False,
        points=[(0,20), (0,0), (20,0), (20,20)], width=10)
    elif pattern == "0010":
      pygame.draw.lines(self.surf, color=self.WALL_COLOR, closed=False,
        points=[(20,20), (0,20), (0,0), (20,0)], width=10)    
    elif pattern == "0011":
      pygame.draw.lines(self.surf, color=self.WALL_COLOR, closed=False,
        points=[(0,20), (0,0), (20,0)], width=10)    
    elif pattern == "0100":
      pygame.draw.lines(self.surf, color=self.WALL_COLOR, closed=False,
        points=[(0,0), (0,20), (20,20), (20, 0)], width=10)
    elif pattern == "0101":
      pygame.draw.line(self.surf, color=self.WALL_COLOR, start_pos=(0,0), end_pos=(0,20), width=10)
      pygame.draw.line(self.surf, color=self.WALL_COLOR, start_pos=(20,0), end_pos=(20,20), width=10)
    elif pattern == "0110":
      pygame.draw.lines(self.surf, color=self.WALL_COLOR, closed=False,
        points=[(0,0), (0,20), (20,20)], width=10)
    elif pattern == "0111":
      pygame.draw.line(self.surf, color=self.WALL_COLOR, start_pos=(0,0), end_pos=(0,20), width=10)
    elif pattern == "1000":
      pygame.draw.lines(self.surf, color=self.WALL_COLOR, closed=False,
        points=[(0,0), (20,0), (20,20), (0,20)], width=10)
    elif pattern == "1001":
      pygame.draw.lines(self.surf, color=self.WALL_COLOR, closed=False,
        points=[(0,0), (20,0), (20,20)], width=10)
    elif pattern == "1010":
      pygame.draw.line(self.surf, color=self.WALL_COLOR, start_pos=(0,0), end_pos=(20,0), width=10)
      pygame.draw.line(self.surf, color=self.WALL_COLOR, start_pos=(0,20), end_pos=(20,20), width=10)
    elif pattern == "1011":
      pygame.draw.line(self.surf, color=self.WALL_COLOR, start_pos=(0,0), end_pos=(20,0), width=10)
    elif pattern == "1100":
      pygame.draw.lines(self.surf, color=self.WALL_COLOR, closed=False,
        points=[(20,0), (20,20), (0,20)], width=10)    
    elif pattern == "1101":
      pygame.draw.line(self.surf, color=self.WALL_COLOR, start_pos=(20,0), end_pos=(20,20), width=10)
    elif pattern == "1110":
      pygame.draw.line(self.surf, color=self.WALL_COLOR, start_pos=(0,20), end_pos=(20,20), width=10)
    # pattern == 1111 => Empty surface

  def __str__(self):
      return self.pattern
