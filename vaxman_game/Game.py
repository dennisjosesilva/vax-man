from typing import Pattern
import pygame 

from vaxman_game.Player import Player
from vaxman_game.Level import Level

from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE)

class Game:

  SCREEN_WIDTH = 800
  SCREEN_HEIGHT = 600

  MULTIPLY_EVENT = pygame.USEREVENT + 1
  MULTIPLY_TIME = 30000    # 30000 Miliseconds = 30 seconds

  def __init__(self):
    pass
    
  def initialize_game(self, level_filename):
    pygame.init()            

    self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))       
    self.level = Level(filename=level_filename)    
    self.SCREEN_WIDTH = self.level.width * 20
    self.SCREEN_HEIGHT = self.level.height * 20    
    self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))       

    initial_number_of_viruses = self.level.number_of_virus()
    self.game_over_number_of_viruses = 32 * initial_number_of_viruses

    self.player = Player(level=self.level, init_pos=self.level.player_pos)
    self.clock = pygame.time.Clock()

    pygame.time.set_timer(self.MULTIPLY_EVENT, self.MULTIPLY_TIME)

    self.has_won = False
    
  def start(self, level_filename):    
    self.initialize_game(level_filename)
    self.running = True

    # Game Loop
    # ---------
    while self.running:
      self.process_events()
      self.draw_frame()
      self.clock.tick(30)

    return self.has_won

  def process_events(self):
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          self.running = False

      elif event.type == QUIT:
        self.running = False

      elif event.type == self.MULTIPLY_EVENT:
        for virus in self.level.viruses:
          virus.multiply() 

    if self.is_game_over_lose():      
      self.has_won = False
      self.running = False
    

    if self.is_game_over_win():
      self.has_won = True
      self.running = False

    self.player.process_collisions()
    pressed_keys = pygame.key.get_pressed()
    self.player.processKeyboard(pressed_keys)
    self.level.update()

  def draw_frame(self):
    # clear the screen
    self.screen.fill((0, 0, 0))
    
    self.level.draw(self.screen)
    self.player.draw(self.screen)
    pygame.display.flip()  

  def is_game_over_lose(self):
    return self.level.number_of_virus() >= self.game_over_number_of_viruses

  def is_game_over_win(self):
    return self.level.number_of_unvaccinated_people() <= 0