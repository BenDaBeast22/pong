import pygame
from constants import *

class Paddle:
  COLOR = WHITE
  VEL = 4

  def __init__(self, x, y, width, height):
    self.x = self.og_x = x
    self.y = self.og_y = y
    self.width = width
    self.height = height

  def draw(self, win):
    pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

  def move(self, up=True):
    if up:
      self.y -= self.VEL
    else:
      self.y += self.VEL
  
  def moveUp(self):
    self.y -= 1

  def moveDown(self):
    self.y += 1

  def reset(self):
    self.x = self.og_x
    self.y = self.og_y

class Ball:
  COLOR = WHITE
  MAX_VEL = 5

  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius = radius
    self.x_vel = self.MAX_VEL
    self.y_vel = 0
  
  def draw(self, win):
    pygame.draw.circle(win, WHITE, (self.x, self.y), self.radius)
  
  def move(self):
    self.x += self.x_vel
    self.y += self.y_vel
  
  def reset(self):
    self.x = WIDTH/2
    self.y = HEIGHT/2
    self.x_vel *= -1
    self.y_vel = 0
    pygame.time.delay(1500)