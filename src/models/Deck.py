#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Card import Card
from models.Minion_Card import Minion_Card
from models.Research_Card import Research_Card

class Deck:
	def __init__(self):
		self.list_of_cards = [Card() for card in range(25)]
		self.card_back = None

	def is_empty(self, ):
		pass

	def shuffle(self, ):
		pass

	def draw(self):
		pass