#!/usr/bin/python
#-*- coding: utf-8 -*-

from models.Card import Card

class Research_Card(Card):
	def __init__(self):
		super(Research_Card, self).__init__()

		self.can_be_placed = False
		self.can_attack = False

	def effect(self, ):
		pass

