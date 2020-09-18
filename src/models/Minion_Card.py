#!/usr/bin/python
#-*- coding: utf-8 -*-

from models.Card import Card

class Minion_Card(Card):
	def __init__(self):
		super(Minion_Card, self).__init__()
		self.health = 0
		self.attack = 0
		self.armor = 0
		self.range = 0

	def attack_entity(self):
		pass

	def die(self, ):
		pass

	def get_damage(self, ):
		pass

	def is_alive(self, ):
		pass

