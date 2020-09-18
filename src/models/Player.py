#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Hero import Hero
from models.Deck import Deck

class Player:
	def __init__(self, side):
		self.deck = Deck()
		self.hero = Hero(side)
		self.health = 20
		self.vault = 0

	def die(self, ):
		pass

	def start_of_turn(self):
		self.deck.draw()
		self.vault += 3

	def end_of_turn(self, ):
		pass

	def is_alive(self, ):
		pass

