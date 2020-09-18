#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

class Entity():
	def __init__(self):
		# render part
		self.rect = pygame.Rect((0,0,200,200))
		self.image = pygame.image.load("resources/sPear.png")

		# to use the drag and drop
		self.click = False


	def render(self, board, side, offset):
		if self.click:
			self.rect.center = pygame.mouse.get_pos()
		board.blit(self.image,self.rect)

	def is_clicked(self,pos):
		return self.rect.collidepoint(pos)
