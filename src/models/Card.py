#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Entity import Entity, pygame

class Card(Entity):
	def __init__(self):
		super(Card, self).__init__()
		self.cost = None


	def play(self):
		pass


	def is_playable(self):
		pass

