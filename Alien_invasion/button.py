import pygame.font
class Button:
	def __init__(self,ai_game,msg):
		self.window = ai_game.window
		self.window_rect = self.window.get_rect()
		self.width, self.height = 200, 50
		self.text_color = (255,255,255)
		self.button_color = (0, 135, 0)
		self.font = pygame.font.SysFont(None, 48)
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.window_rect.center
		self._prep_msg(msg)
	def _prep_msg(self,msg):
		self.msg_image = self.font.render(msg, False, self.text_color, self.button_color)#блять что это(заебать дип сик)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	def draw_button(self):
		self.window.fill(self.button_color, self.rect)
		self.window.blit(self.msg_image, self.msg_image_rect)