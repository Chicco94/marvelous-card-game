#!/usr/bin/python
#-*- coding: utf-8 -*-

from Minion Card import Minion Card
from Research Card import Research Card

class Card(Minion Card, Research Card):
	def __init__(self):
		self.cost = None

	def play(self, ):
		pass

	def is_playable(self, ):
		pass

