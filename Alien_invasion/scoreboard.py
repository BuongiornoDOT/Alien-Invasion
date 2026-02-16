import os
import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard:
	def __init__(self, ai_game, record_file = 'record.txt'):
		self.ai_game = ai_game
		self.file_name = record_file
		self.window = ai_game.window
		self.window_rect = self.window.get_rect()
		self.setting = ai_game.setting
		self.stats = ai_game.stats
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		self.prep_score()
		self.prep_level()
		self.prep_ships()
		self.load_high_score()
	def load_high_score(self):
		if os.path.exists(self.file_name):
			with open(self.file_name, 'r', encoding = 'utf-8') as  file:
				data = file.read()
				self.stats.high_score = int(data)
		else:
			with open(self.file_name, 'w', encoding = 'utf-8') as file:
				file.write(str(0))
	def save_high_score(self):
		with open(self.file_name, 'w', encoding = 'utf-8') as  file:
			file.write(str(self.stats.score))
			self.prep_score()
	def prep_score(self):
		rounded_score = round(self.stats.score, -1)
		rounded_high_score = round(self.stats.high_score, -1)
		score_str = f'{rounded_score:,}'
		high_score_str = f'{rounded_high_score:,}'
		self.score_image = self.font.render(score_str, False,self.text_color, self.setting.bg_collor)
		self.high_score_image = self.font.render(high_score_str, False,self.text_color, self.setting.bg_collor)
		self.score_rect = self.score_image.get_rect()
		self.high_score_rect = self.high_score_image.get_rect()
		self.score_rect.right = self.window_rect.right - 20
		self.high_score_rect.center = self.window_rect.center
		self.score_rect.top = 20
		self.high_score_rect.top = 20
	def prep_level(self):
		level_str = str(self.stats.lvl)
		self.level_image = self.font.render(level_str, False, self.text_color, self.setting.bg_collor)
		self.lvl_rect = self.level_image.get_rect()
		self.lvl_rect.right = self.score_rect.right
		self.lvl_rect.top = self.score_rect.bottom + 10
	def show_score(self):
		self.window.blit(self.score_image, self.score_rect)
		self.window.blit(self.high_score_image, self.high_score_rect)
		self.window.blit(self.level_image, self.lvl_rect)
		self.ships.draw(self.window)
	def prep_ships(self):
		self.ships = Group()
		if self.ai_game.game_active == True:
			for ship_number in range(self.stats.ships_left):
				ship = Ship(self.ai_game)
				ship.rect.x = 10 + ship_number * ship.rect.width
				ship.rect.y = 10
				self.ships.add(ship)
				print('ok')