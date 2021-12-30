import pygame 
import os

from vaxman_game.Level import Level 

from enum import Enum

from pygame.locals import (
  KEYDOWN, KEYUP, QUIT, K_ESCAPE,
  K_ESCAPE, K_RIGHT, K_LEFT, K_RETURN)


class LevelSelector:
  SCREEN_WIDTH = 800
  SCREEN_HEIGHT = 600

  class LevelInfo:
    def __init__(self, level_name, filename):
      self.name = level_name
      self.filename = filename  

  def __init__(self):
    self.setup_available_levels()
    self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT)) 
    self.cur_level = 0
    self.is_key_down = False    
    pygame.font.init()
    self.font = pygame.font.SysFont("Comic Sans MS", 42)

  def draw_level_surface(self):
    info = self.level_info[self.cur_level]
    
    # Draw image of the level
    # -----------------------
    level = Level(info.filename)
    level_surface = pygame.Surface((level.width*20, level.height*20))
    level.draw(level_surface)
    
    level_area_size = (360, 420)

    level_area = pygame.Surface(level_area_size)
    level_area_rect = level_area.get_rect()
    level_area_rect.move_ip(220, 25)

    s = pygame.transform.scale(level_surface, level_area_size)    
    self.screen.blit(s, level_area_rect)

    # Draw name of the level
    # ----------------------
    level_name_surface = self.font.render(info.name, False, (255, 255, 255))
    name_rect = level_name_surface.get_rect()
    name_rect.move_ip(400 - (name_rect.width/2), 460)
    self.screen.blit(level_name_surface, name_rect)

    # Draw instruction
    # ----------------
    instr_text_surface = self.font.render("Press ENTER to start the game, or ESC for quit the game", 
      False, (255, 255, 255))
    instr_rect = instr_text_surface.get_rect()
    instr_rect.move_ip(400 - (instr_rect.width/2), 510)
    self.screen.blit(instr_text_surface, instr_rect)

  def setup_available_levels(self):
    filenames = os.listdir("levels") 
    self.level_info = []
    for f in filenames:
      self.level_info.append(self.LevelInfo(self.process_name(f), "levels/"+f))      

  def process_name(self, name):
    n = name[:-4]
    return n.replace("_", " ")

  def get_selected_level(self):
    self.running = True    
    self.clock = pygame.time.Clock()

    level_filename = None 

    while self.running:
      for event in pygame.event.get():
        if event.type == QUIT:
          self.running = False

        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            self.running = False

          if event.key == K_RIGHT and not self.is_key_down:
            self.move_level_to_right()
            self.is_key_down = True
          
          elif event.key == K_LEFT and not self.is_key_down:
            self.move_level_to_left()
            self.is_key_down = True

          if event.key == K_RETURN:
            info = self.level_info[self.cur_level]
            level_filename = info.filename
            self.running = False

          if event.key == K_ESCAPE:
            level_filename = None 
            self.running = False

        if event.type == KEYUP:
          if event.key == K_RIGHT and self.is_key_down:            
            self.is_key_down = False
          
          elif event.key == K_LEFT and self.is_key_down:
            self.is_key_down = False
      
      self.screen.fill((0, 0, 0))
      self.draw_level_surface()
      pygame.display.flip()  
      self.clock.tick(120)

    return level_filename 

  
  def move_level_to_left(self):
    if 0 < self.cur_level:
      self.cur_level -= 1
      
  def move_level_to_right(self):
    if self.cur_level < len(self.level_info)-1:
      self.cur_level += 1
      