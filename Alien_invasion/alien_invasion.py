import sys
from time import sleep
import pygame
import math
from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
class AlienInvasion:
	def __init__(self):
		pygame.init()
		self.setting = Setting()
		self.window = pygame.display.set_mode((self.setting.window_width,self.setting.window_height))
		pygame.display.set_caption('Alion Invasion')
		self.stats = GameStats(self)
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.frame_rate = pygame.time.Clock()
		self._create_fleet()
		self.game_active = False
		self.play_button = Button(self, 'Play')
		self.sb = Scoreboard(self)
	def run_game(self):
		while True:
			self._chek_events()
			self._update_screen()
			self.frame_rate.tick(60)
			if self.game_active:
				self.ship.update()
				self.bullets.update()
				self._update_aliens()
				self._check_bullet_position()
	def _chek_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
			if self.game_active:
				if event.type == pygame.KEYDOWN:
					self._chek_event_keydown(event)
				elif event.type == pygame.KEYUP:
					self._chek_event_keyup(event)
	def _update_screen(self):
		self.window.fill(self.setting.bg_collor)
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.ship.blitme()
		self.aliens.draw(self.window)
		self.check_high_score()
		self.sb.show_score()
		if not self.game_active:
			self.play_button.draw_button()
		pygame.display.flip()
	def _chek_event_keydown(self,event):
		if event.key == pygame.K_d:
			self.ship.move_right = True
		elif event.key == pygame.K_a:
			self.ship.move_left = True
		elif event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self.fire_bullet()
	def fire_bullet(self):
		current_time = pygame.time.get_ticks()
		if current_time - self.setting.last_shot >= self.setting.cooldown_shot:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
			self.setting.last_shot = current_time
	def _check_bullet_position(self):
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
			collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,False)
			if collisions:
				for aliens in collisions.values():
					alien = aliens[0]
					self.aliens.remove(alien)
					self.stats.score += self.setting.alien_points
					self.sb.prep_score()
			if not self.aliens:
				self.bullets.empty()
				self._create_fleet()
				self.setting.increase_speed()
				self.stats.lvl += 1
				self.sb.prep_level()
	def _chek_event_keyup(self,event):
		if event.key == pygame.K_d:
				self.ship.move_right = False
		elif event.key == pygame.K_a:
				self.ship.move_left = False
	def _create_fleet(self):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		current_x,current_y = alien_width, alien_height
		while current_y < self.setting.window_height - 3 * alien_height:
			while current_x < self.setting.window_width - 2 * alien_width:
				self._create_alien(current_x,current_y)
				current_x += 2 * alien_width
			current_x = alien_width
			current_y += alien_height
	def _create_alien(self, x_position, y_position):
		new_alien = Alien(self)
		new_alien.x = x_position
		new_alien.rect.x = x_position
		new_alien.rect.y = y_position
		self.aliens.add(new_alien)
	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self.change_fleet_direction()
				break
	def change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.setting.alien_drop_speed
		self.setting.fleet_direction *= -1
	def _update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		self._check_aliens_bottom()
	def _ship_hit(self):
		self.aliens.empty()
		self.bullets.empty()
		self._create_fleet()
		self.ship.centr_ship()
		if self.stats.ships_left > 1:
			self.stats.ships_left -= 1
			sleep(0.5)
			self.sb.prep_ships()
		else:
			self.game_active = False
			pygame.mouse.set_visible(True)
			self.sb.prep_ships()
	def _check_aliens_bottom(self):
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= self.setting.window_height:
				self._ship_hit()
	def _check_play_button(self, mouse_pos):
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.game_active:
			self.setting.initialize_settings()
			self.aliens.empty()
			self.bullets.empty()
			self._create_fleet()
			self.ship.centr_ship()
			self.stats.reset_stats()
			self.sb.prep_score()
			self.game_active = True
			self.sb.prep_ships()
			pygame.mouse.set_visible(False)
	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.sb.save_high_score()
if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()