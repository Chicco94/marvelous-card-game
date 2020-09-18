#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Hero import Hero
from models.Deck import Deck

class Player:
	def __init__(self):
		self.deck = None
		self.hero = None
		self.Health = None
		self.Vault = None

	def die(self, ):
		pass

	def start_of_turn(self, ):
		pass

	def end_of_turn(self, ):
		pass

	def is_alive(self, ):
		pass

