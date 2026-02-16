import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	def __init__(self,main):
		super().__init__()
		self.display = main.window
		self.setting = main.setting
		self.color = self.setting.bullet_collor
		self.rect = pygame.Rect(0,0, self.setting.bullet_width, self.setting.bullet_height)
		self.rect.midtop = main.ship.rect.midtop
		self.y = float(self.rect.y)
	def update(self):
		self.y -= self.setting.bullet_speed
		self.rect.y = self.y 
	def draw_bullet(self):
		pygame.draw.rect(self.display,self.color,self.rect)