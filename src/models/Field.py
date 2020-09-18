#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Player import Player
from models.Place import Place, pygame
from models.Card import Card

class Field:
	def __init__(self, side):
		# two line of combat
		if side is 0:
			self.minion_slots = [Place((360,310)),Place((460,310)),Place((560,310)),Place((260,210)),Place((360,210)),Place((460,210)),Place((560,210)),Place((660,210))]
		else:
			self.minion_slots = [Place((360,610)),Place((460,610)),Place((560,610)),Place((260,710)),Place((360,710)),Place((460,710)),Place((560,710)),Place((660,710))]
		self.player = Player(side)
		self.hand = [Card() for x in range(5)]
		self.side = side

	def render(self, board):
		# posiziono i minion
		for place in self.minion_slots:
			place.render(board)

		# posiziono la mano del giocatore
		offsets = [(700,100), (300,900)]
		for card in self.hand:
			if card:
				card.render(board, offsets[self.side])

		# posiziono l'eroe
		self.player.hero.render(board)

	def get_clicked_entity(self,pos):
		for place in self.minion_slots:
			if place and place.is_clicked(pos):
				return place
		for card in self.hand:
			if card and card.is_clicked(pos):
				return card
		if self.player.hero.is_clicked(pos):
			return self.player.hero
		
	def is_valid_place(self, entity):
		''' find if an entity is moved over an enmpty place,
			if so, returns it
		'''
		for place in self.minion_slots:
			if place.is_free() and entity.is_over(place):
				return place
		return None


