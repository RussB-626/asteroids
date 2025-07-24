import pygame
import random
import math
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
  def update(self, dt):
    self.position += (self.velocity * dt)

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    # randomize the angle of the split
    random_angle = math.floor(random.uniform(20, 50))

    rotation_a = self.velocity.rotate(random_angle)
    rotation_b = self.velocity.rotate(-random_angle)
    
    new_radius = self.radius - ASTEROID_MIN_RADIUS

    asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid_one.velocity = rotation_a * 1.2

    asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid_two.velocity = rotation_b * 1.2