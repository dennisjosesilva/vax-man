import pygame

from pygame.locals import (
  QUIT, KEYDOWN, 
  K_RETURN
)

class GameOverScreen(pygame.sprite.Sprite):
  def __init__(self, won=True):
    self.screen = pygame.display.set_mode((480, 230))
    if won:
      self.define_won_screen()
    else:
      self.define_lose_screen()    

  def start(self):
    self.running = True

    while self.running:
      for event in pygame.event.get():
        if event.type == QUIT:
          self.running = False
        elif event.type == KEYDOWN:
          if event.key == K_RETURN:
            self.running = False

      self.draw()

  def define_won_screen(self):                
    self.surf = pygame.image.load("images/game_over_win.png").convert()
    self.rect = self.surf.get_rect()

  def define_lose_screen(self):
    self.surf = pygame.image.load("images/game_over_lose.png").convert()
    self.rect = self.surf.get_rect()

  def draw(self):
    self.screen.fill((0,0,0))
    self.screen.blit(self.surf, self.rect)
    pygame.display.flip()

