#!/usr/bin/python
#-*- coding: utf-8 -*-
from models.Board import Board,pygame

class Game:
	def __init__(self, screen_width  = 800, screen_height = 600):
		self.board = Board(800,600)


	def turn(self, ):
		pass


	def start_of_game(self):
		# set main variables
		self.game_ended = False
		self.keep_going = True # variable to exit the game
		self.turn_time = 30

		# start the main loop
		self.main_loop()


	def end_game(self):
		pass


	def main_loop(self):
		while self.keep_going:
			self.board.render()

			self.board.handle_event()

			pygame.display.update()



	def is_game_ended(self) -> bool:
		return False



