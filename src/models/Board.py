#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Field import Field, pygame
from models.Player import Player

class Board:
	def __init__(self, screen_width  = 800, screen_height = 600):
		self.fields = [Field(x) for x in range(8)]
		
		pygame.init()
		
		# Title and icon
		pygame.display.set_caption("Marvelous card game")
		pygame.display.set_icon(pygame.image.load("resources/logo.jpg"))
		self.screen = pygame.display.set_mode((screen_width,screen_height))

		self.clicked_entity = None
		self.player = Player(1)
		self.opponent = Player(0)

	def render(self):
		self.screen.fill((255,255,255))
		self.screen.blit(pygame.image.load("resources/background.png"),(0,0))
		
		for field in self.fields:
			field.render(self.screen)
		
		self.player.render(self.screen)
		self.opponent.render(self.screen)

	def get_clicked_entity(self,pos):
		for field in self.fields:
			for place in field.minion_slots:
				if place and place.is_clicked(pos):
					return place
		for card in self.player.hand:
			print("ho cliccato una carta1",pos , card.is_clicked(pos))
			print(card.rect.center)
			if card and card.is_clicked(pos):
				return card
		if self.player.hero.is_clicked(pos):
			return self.player.hero


	def handle_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
			# player interactions
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos
				entity = self.get_clicked_entity(pos)
				if entity and entity.can_be_moved:
					entity.click = True
					self.clicked_entity = entity
			if event.type == pygame.MOUSEBUTTONUP:
				print(self.clicked_entity)
				if self.clicked_entity and self.clicked_entity.can_be_placed:
					for field in self.fields:
						place = field.is_valid_place(self.clicked_entity)
						print(field.is_valid_place(self.clicked_entity))
						if place:
							place.set_entity(self.clicked_entity)
							self.player.hand.remove(self.clicked_entity)
							break
					self.clicked_entity.click = False



