#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Hero import Hero
from models.Deck import Deck
from models.Card import Card

class Player:
	def __init__(self, side):
		self.deck = Deck()
		self.hero = Hero(side)
		self.health = 20
		self.vault = 0
		self.hand = [Card() for x in range(5)]
		self.side = side

	def die(self, ):
		pass

	def start_of_turn(self):
		self.deck.draw()
		self.vault += 3

	def end_of_turn(self, ):
		pass

	def is_alive(self, ):
		pass

	def render(self, board):
		self.hero.render(board)

		# posiziono la mano del giocatore
		offsets = [(700,100), (300,900)]
		for i,card in enumerate(self.hand):
			if card:
				card.render(board, (offsets[self.side][0]+i*80,offsets[self.side][1]))

