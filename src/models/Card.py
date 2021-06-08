#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Entity import Entity, pygame

class Card(Entity):
	def __init__(self, image):
		super(Card, self).__init__()
		self.cost = None
		self.image = image


	def play(self, pos):
		self.image_size = 80
		self.rect.center = pygame.Rect((pos[0],pos[1],self.image_size,self.image_size))


	def is_playable(self):
		pass

