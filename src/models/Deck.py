#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Card import Card, pygame
from models.Minion_Card import Minion_Card
from models.Research_Card import Research_Card
import random

class Deck:
	def __init__(self):
		knight_image = pygame.image.load("resources/knight.jpg")
		spear_image = pygame.image.load("resources/spearman.png")
		archer_image = pygame.image.load("resources/archer.jpg")
		shield_image = pygame.image.load("resources/shieldman.jpg")
		self.list_of_cards = []

		for x in range(5):
			self.list_of_cards.append(Card(knight_image))
		for x in range(5):
			self.list_of_cards.append(Card(spear_image))
		for x in range(5):
			self.list_of_cards.append(Card(archer_image))
		for x in range(5):
			self.list_of_cards.append(Card(shield_image))
			
		self.card_back = None

	def is_empty(self) -> bool:
		return len(self.list_of_cards)==0

	def shuffle(self) -> None:
		random.shuffle(self.list_of_cards)

	def draw(self) -> Card:
		return self.list_of_cards.pop()