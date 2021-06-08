#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Card import Card, pygame
from models.Minion_Card import Minion_Card
from models.Research_Card import Research_Card

class Deck:
	def __init__(self):
		card_image_1 = pygame.image.load("resources/spear.png")
		card_image_2 = pygame.image.load("resources/sword.png")
		self.list_of_cards = [Card(card_image_1 if card%2 else card_image_2) for card in range(25)]
		self.card_back = None

	def is_empty(self, ):
		pass

	def shuffle(self, ):
		pass

	def draw(self):
		pass