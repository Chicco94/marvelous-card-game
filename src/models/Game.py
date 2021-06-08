#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Board import Board,pygame,possibleActions
from time import sleep
from threading import Thread

from models.Player import Player

STOP_TURN = False
class Game:
	def __init__(self, screen_width  = 1000, screen_height = 1000):
		self.board = Board(screen_width,screen_height)
		self.turn_ended = False

	def turn(self, player:Player):
		print("start turn")
		self.turn_ended = False
		player.draw()
		while not self.turn_ended:
			pass
		

	def start_timer_turn(self):
		global STOP_TURN
		while not self.turn_ended and not STOP_TURN:
			self.turn_ended = False
		self.turn_ended = True


	def start_of_game(self):
		# set main variables
		self.game_ended = False
		self.keep_going = True # variable to exit the game
		self.turn_time = 30

		print("sto partendo")
		main_game = Thread(target=self.main_game())
		main_game.start()

		self.render_loop()
		main_game.join()


	def main_game(self):
		global STOP_TURN

		# shuffle decks
		self.board.player.deck.shuffle()
		self.board.opponent.deck.shuffle()
		print("shuffled decks")
		
		# draw 5 cards each
		for _ in range(5):
			self.board.player.draw()
			self.board.opponent.draw()
		print("drew cards")

		# alternate of turns
		while self.keep_going:
			self.board.render()
			reuslt = self.board.handle_event()
			if reuslt == possibleActions.END_TURN:
				STOP_TURN=True
			pygame.display.update()

			if not self.turn:
				STOP_TURN = False
				self.timer = Thread(target=self.start_timer_turn())
				self.turn = Thread(target=self.turn(self.board.player))
				self.timer.start()
				self.turn.start()
				self.timer.join(30)
				self.turn.join()


	def check_end_game(self):
		if self.end_game():
			self.keep_going = False
		print("end game")


	def end_game(self):
		return not self.board.player.is_alive() or not self.board.opponent.is_alive()


	def render_loop(self):
		print("render loop")


	def is_game_ended(self) -> bool:
		return False



