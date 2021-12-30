import pygame

import vaxman_game

from enum import Enum

from pygame.locals import (
  K_UP, K_DOWN, K_LEFT, K_RIGHT
)

class Player(pygame.sprite.Sprite):

  def __init__(self, level, init_pos=(0,0)):
    super(Player, self).__init__()
    self.surf = pygame.Surface((12, 12))    
    self.surf = pygame.image.load("images/vaccine.png").convert()
    self.level = level 
    self.speed = 2
    
    self.screen_width = level.width * 20
    self.screen_height = level.height * 20

    self.rect = self.surf.get_rect(
      center=(init_pos[0]+10, init_pos[1]+10))

  def has_a_wall_collision(self):    
    return pygame.sprite.spritecollideany(self, self.level.wall_tiles)

  def moveLeft(self):
    self.rect.move_ip(-self.speed, 0)
    if self.has_a_wall_collision():
      self.rect.move_ip(self.speed, 0)    

    if self.rect.right < 0:      
      self.rect.left = self.screen_width
  
  def moveRight(self):    
    self.rect.move_ip(self.speed, 0)    
    if self.has_a_wall_collision():
      self.rect.move_ip(-self.speed, 0)

    if self.rect.left >= self.screen_width:
      self.rect.right = 0

  def moveDown(self):
    self.rect.move_ip(0, self.speed)
    if self.has_a_wall_collision():
      self.rect.move_ip(0, -self.speed)

    if self.rect.top >= self.screen_height:
      self.rect.bottom = 0

  def moveUp(self):
    self.rect.move_ip(0, -self.speed)
    if self.has_a_wall_collision():
      self.rect.move_ip(0, self.speed)

    if self.rect.bottom <= 0:
      self.rect.top = self.screen_height

  def processKeyboard(self, pressed_keys):
    if pressed_keys[K_UP]:
      self.moveUp()
    if pressed_keys[K_DOWN]:
      self.moveDown()
    if pressed_keys[K_RIGHT]:
      self.moveRight()
    if pressed_keys[K_LEFT]:
      self.moveLeft()  

  def process_collisions_by_group(self, group):
    collision = pygame.sprite.spritecollideany(self, group)
    if collision:
      collision.kill()

  def process_collisions(self):
    self.process_collisions_by_group(self.level.person_tiles)
    self.process_collisions_by_group(self.level.viruses)

  def draw(self, screen):
    screen.blit(self.surf, self.rect)