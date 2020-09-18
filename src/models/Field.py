#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Player import Player
from models.Minion_Card import Minion_Card
from models.Card import Card, pygame

class Field:
	def __init__(self):
		# two line of combat
		self.first_line = [Minion_Card() for x in range(4)]
		self.second_line = [Minion_Card() for x in range(4)]
		self.player = Player()
		self.hand = []
		self.side = 0

	def render(self, board, side):
		offset = 0
		for minion in self.first_line:
			minion.render(board, side, offset)
		for minion in self.second_line:
			minion.render(board, side, offset)
		for card in self.hand:
			card.render(board,side, offset)
		self.player.hero.render(board,side)

	def get_clicked_entity(self,pos):
		for minion in self.first_line:
			if minion.is_clicked(pos):
				return minion
		for minion in self.second_line:
			if minion.is_clicked(pos):
				return minion
		for card in self.hand:
			if card.is_clicked(pos):
				return card
		if self.player.hero.is_clicked(pos):
			return self.player.hero
		


