from pygame import *
from math import * 

class Seesaw:
	def __init__(self):
		self.pic = image.load("plate.png")
		self.start = -1000   # starting angle when moving right
		self.end = 1000  # ending angle when moving right
		self.moveLeft  = False  
		self.moveRight = False
		self.stick = image.load("plate.png")
		self.s2 = transform.rotate(self.stick,radians(-1000)) # seesaw starts off like this
	
	def draw(self, screen):
		x = 300 - self.s2.get_width()/2
		y = 650 - self.s2.get_height()/2
		screen.blit(self.s2, (x,y))

	def rotate(self):
		if self.moveRight:
			self.right()
		if self.moveLeft:
			self.left()

	def right(self):
	    # Seesaw moving towards bottom right.
	    if self.start <= 1000:
	        self.s2 = transform.rotate(self.stick, radians(self.start))
	        if self.start > -1000:
	            self.start -= 100   # subtracts 100 until it hits -1000 which = moving right
	        if self.start == -1000: # since we're adding by 100 the seesaw doesnt have the gliding effect (its too fast)
	            self.moveRight = False
	            self.start = -1000 
	        
	def left(self):
	    # Seesaw moving towards bottom left.
	    if self.end >= -1000:
	    	self.s2 = transform.rotate(self.stick,radians(self.end))
	        if self.end < 1000:
	            self.end += 100 # adds 100 until it hits 1000 which = moving left
	        if self.end == 1000:
	            self.moveLeft = False
	            self.end = 1000