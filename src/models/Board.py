#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Field import Field, pygame

class Board:
	def __init__(self, screen_width  = 800, screen_height = 600):
		self.fields = [Field(),Field()]
		
		pygame.init()
		
		# Title and icon
		pygame.display.set_caption("Marvelous card game")
		pygame.display.set_icon(pygame.image.load("resources/logo.jpg"))
		self.screen = pygame.display.set_mode((screen_width,screen_height))

		self.clicked_entity = None

	def render(self):
		self.screen.fill((255,255,255))
		self.screen.blit(pygame.image.load("resources/background.png"),(0,0))
		self.fields[0].render(self.screen,0)
		self.fields[1].render(self.screen,1)


	def handle_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
			# player interactions
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos
				entity = self.fields[0].get_clicked_entity(pos)
				entity.click = True
				self.clicked_entity = entity
			if event.type == pygame.MOUSEBUTTONUP:
				self.clicked_entity.click = False



