class Setting:
	def __init__(self):
		self.window_width = 720
		self.window_height = 480
		self.bg_collor = (91,121,94)
		self.bullet_collor = (255,0,0)
		self.bullet_width = 6
		self.bullet_height = 30
		self.alien_drop_speed = 10
		self.ship_limit = 3
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.alien_points = 50
		self.last_shot = 0
		self.cooldown_shot = 500
		self.initialize_settings()
	def initialize_settings(self):
		self.speed = 4
		self.bullet_speed = 8
		self.alien_speed = 2
		self.fleet_direction = 1
		self.alien_points = 50
	def increase_speed(self):
		self.speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)