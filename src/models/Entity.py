#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

class Entity():
	def __init__(self):
		# render part
		self.image = pygame.image.load("resources/sPear.png")
		self.image_size = 200
		self.rect = pygame.Rect((0,0,self.image_size,self.image_size))

		# to use the drag and drop
		self.click = False


	def render(self, board, offset = None):
		if self.click:
			self.rect.center = pygame.mouse.get_pos()
		elif offset:
			self.rect.center = (offset[0],offset[1])
		board.blit(self.image,self.rect)

	def is_clicked(self,pos):
		return self.rect.collidepoint(pos)
