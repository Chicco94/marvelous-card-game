#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Place import Place, pygame

class Field:
	def __init__(self, side):
		# two line of combat
		self.minion_slots = [Place((side*100+100,x*100+100)) for x in range(8)]
		self.side = side

	def render(self, board):
		# posiziono i minion
		for place in self.minion_slots:
			place.render(board)

	def is_valid_place(self, pos):
		''' find if an entity is moved over an enmpty place,
			if so, returns it
		'''
		for place in self.minion_slots:
			if place.is_free() and place.mouse_over(pos):
				return place
		return None


