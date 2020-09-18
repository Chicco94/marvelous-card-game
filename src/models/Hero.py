#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Entity import Entity, pygame
class Hero(Entity):
	def __init__(self, side):
		super(Hero, self).__init__()
		self.name = None
		offsets = [(500,100), (500,900)]
		self.rect.center = offsets[side]

	def hero_power(self, ):
		pass

