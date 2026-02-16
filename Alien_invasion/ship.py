import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	def __init__(self,ai_game):
		super().__init__()
		self.settings = ai_game.setting
		self.window = ai_game.window
		self.widow_rect = ai_game.window.get_rect()
		self.image = pygame.image.load("ship.png")
		self.rect = self.image.get_rect()
		self.rect_width = int(self.rect.width)
		self.window_width = int(self.widow_rect.width)
		self.rect.midbottom = self.widow_rect.midbottom
		self.x = float(self.rect.x)
		self.move_right = False
		self.move_left = False
	def blitme(self):
		self.window.blit(self.image, self.rect)
	def update(self):
		if self.move_right:
			max_x = self.window_width - self.rect_width
			self.x = min(self.x + self.settings.speed,max_x)
		elif self.move_left:
			self.x = max(self.x - self.settings.speed,0)
		self.rect.x = self.x
	def centr_ship(self):
		self.rect.midbottom = self.widow_rect.midbottom
		self.x = float(self.rect.x)