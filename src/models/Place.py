#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Entity import Entity, pygame

class Place(Entity):
	def __init__(self, pos):
		super(Place, self).__init__()
		# two line of combat
		self.entity = None
		self.image = pygame.image.load("resources/place.png")
		self.image_size = 80
		self.rect = pygame.Rect((pos[0],pos[1],self.image_size,self.image_size))

		self.can_be_placed = False
		self.can_be_moved = False
		self.can_be_played = False
		self.can_attack = False

	def is_free(self):
		return self.entity == None

	def set_entity(self,entity):
		self.entity = entity
		self.image = pygame.transform.scale(entity.image,(80,80))
