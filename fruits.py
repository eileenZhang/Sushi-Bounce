
from math import *

class Fruit:
	def __init__(self, name, x, y, score, direction, speed, special, pic):
		self.name = name
		self.x = x
		self.y = y
		self.score = score
		self.speed = speed
		self.special = special
		self.pic = pic

	def move(self):
		self.x += self.speed