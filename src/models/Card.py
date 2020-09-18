#!/usr/bin/python
#-*- coding: utf-8 -*-

from Minion_Card import Minion_Card
from Research_Card import Research_Card

class Card(Minion_Card, Research_Card):
	def __init__(self):
		self.cost = None

	def play(self, ):
		pass

	def is_playable(self, ):
		pass

