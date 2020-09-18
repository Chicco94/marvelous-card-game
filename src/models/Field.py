#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Player import Player
from models.Minion_Card import Minion_Card
from models.Card import Card, pygame

class Field:
	def __init__(self, side):
		# two line of combat
		self.first_line = [None for x in range(3)]
		self.second_line = [None for x in range(5)]
		self.player = Player(side)
		self.hand = [Minion_Card() for x in range(5)]
		self.side = side

	def render(self, board):
		# posiziono la prima linea
		if self.side == 1:
			offsets = [(380,310),(480,310),(580,310)]
		else:
			offsets = [(380,610),(480,610),(580,610)]
		for minion in self.first_line:
			if minion:
				minion.render(board, offsets[self.first_line.index(minion)])

		# posiziono la seconda linea
		if self.side == 1:
			offsets = [(280,210),(380,210),(480,210),(580,210),(680,210)]
		else:
			offsets = [(280,710),(380,710),(480,710),(580,710),(680,710)]

		for minion in self.second_line:
			if minion:
				minion.render(board, offsets[self.second_line.index(minion)])

		# posiziono la mano del giocatore
		offsets = [(700,100), (300,900)]
		for card in self.hand:
			if card:
				card.render(board, offsets[self.side])

		# posiziono l'eroe
		self.player.hero.render(board)

	def get_clicked_entity(self,pos):
		for minion in self.first_line:
			if minion and minion.is_clicked(pos):
				return minion
		for minion in self.second_line:
			if minion and minion.is_clicked(pos):
				return minion
		for card in self.hand:
			if card and card.is_clicked(pos):
				return card
		if self.player.hero.is_clicked(pos):
			return self.player.hero
		


