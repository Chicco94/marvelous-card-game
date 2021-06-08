#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Entity import Entity, pygame
class Hero(Entity):
	def __init__(self, side):
		super(Hero, self).__init__()
		self.name = None
		offsets = [(20,20), (980,980)]
		self.rect.center = offsets[side]

		self.player = side

		self.can_be_played = False
		self.can_be_moved = False
		self.can_be_placed = False

	def hero_power(self, ):
		pass

