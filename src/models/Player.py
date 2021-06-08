#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Hero import Hero
from models.Deck import Deck
from models.Card import Card, pygame

class Player:
	def __init__(self, side):
		self.deck = Deck()
		self.hero = Hero(side)
		self.health = 20
		self.vault = 0
		self.hand = []
		self.side = side

	def die(self, ):
		pass

	def start_of_turn(self):
		self.hand.append(self.deck.draw())
		self.vault += 3

	def end_of_turn(self, ):
		pass

	def is_alive(self) -> bool:
		return self.health == 0

	def draw(self) -> None:
		self.hand.append(self.deck.draw())

	def render(self, board):
		self.hero.render(board)

		# posiziono la mano del giocatore
		offsets = [(700,100), (300,900)]
		for i,card in enumerate(self.hand):
			if card:
				card.render(board, (offsets[self.side][0]+i*80,offsets[self.side][1]))

