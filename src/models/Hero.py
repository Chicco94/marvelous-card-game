#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Entity import Entity, pygame
class Hero(Entity):
	def __init__(self, side):
		super(Hero, self).__init__()
		self.name = None
		offsets = [(500,100), (500,900)]
		self.rect.center = offsets[side]

		self.can_be_played = False
		self.can_be_moved = False
		self.can_be_placed = False

	def hero_power(self, ):
		pass

