import pygame

from enum import Enum
import random

from vaxman_game.graph.LevelGraph import LevelGraph 

class Virus(pygame.sprite.Sprite):  

  def __init__(self, level, init_pos=(0,0), level_pos=(0, 0), multiply_time=3000):
    super(Virus, self).__init__()
#    self.surf = pygame.Surface((12, 12))
    self.surf = pygame.image.load("images/virus.png").convert()    
    self.level = level 
    self.level_pos = level_pos

    self.multiply_time = multiply_time

    self.speed = 2
    self.number_steps = 20 / self.speed

    self.cur_path = self.get_new_path()
    self.curr_move = self.cur_path.pop(0)
    self.cur_move_steps = self.number_steps

    self.rect = self.surf.get_rect()  
    self.rect.move_ip((init_pos[0]+4, init_pos[1]+4))

  def get_new_path(self):
    t = self.level.graph.get_a_random_vertex_pos()    
    path = []
    while path == []:
      path , _, _, _ = self.level.graph.shortest_path(orig=self.level_pos, target=t)

    return path 
    
  def move_left(self):
    self.rect.move_ip(-self.speed, 0) 

  def move_right(self):
    self.rect.move_ip(self.speed, 0)

  def move_down(self):
    self.rect.move_ip(0, self.speed) 

  def move_up(self):
    self.rect.move_ip(0, -self.speed)

  def update(self):
    if self.cur_path == []:      
      self.cur_path = self.get_new_path()
      self.curr_move = self.cur_path.pop(0)
      self.cur_move_steps = self.number_steps

    elif self.cur_move_steps == 0:       
      if self.curr_move == LevelGraph.Move.LEFT:
        self.level_pos = (self.level_pos[0], self.level_pos[1]-1)    
      if self.curr_move == LevelGraph.Move.RIGHT:
        self.level_pos = (self.level_pos[0], self.level_pos[1]+1)
      if self.curr_move == LevelGraph.Move.DOWN:
        self.level_pos = (self.level_pos[0]+1, self.level_pos[1])
      if self.curr_move == LevelGraph.Move.UP:
        self.level_pos = (self.level_pos[0]-1, self.level_pos[1])
                    
      self.curr_move = self.cur_path.pop(0)
      self.cur_move_steps = self.number_steps 
      
    else:
      if self.curr_move == LevelGraph.Move.LEFT:
        self.move_left()    
      if self.curr_move == LevelGraph.Move.RIGHT:
        self.move_right()
      if self.curr_move == LevelGraph.Move.DOWN:
        self.move_down()
      if self.curr_move == LevelGraph.Move.UP:
        self.move_up()

      self.cur_move_steps = self.cur_move_steps - 1

        
  def multiply(self):
    new_virus = Virus(
      level=self.level,
      init_pos=(self.level_pos[1] * 20, self.level_pos[0] * 20),
      level_pos=self.level_pos)
    self.level.viruses.add(new_virus)
    