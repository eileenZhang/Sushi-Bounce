
from pygame import *

GRAV = 0.5
mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)  # must init the mixer first (just like init() but with sounds)
mySound = mixer.Sound                                             # short cut
boing = mySound('boing.wav')                                      # loading a sound; bouncing sound

class Player:
	def __init__(self,name, x, y, vy, up, down, onplate, seesaw, left_bound, right_bound):
		self.name = name
		self.x = x
		self.y = y
		self.vy = vy
		self.up = up
		self.down = down
		self.onPlate = onplate
		self.left_bound = left_bound
		self.right_bound = right_bound

	def bounceDown(self, p2, seesaw):
		# Bouncing down.
	    self.y += self.vy # velocity added to y value (moving down)
	    self.vy+= GRAV   # increasing velocity
	    if self.name == "p2":
	    	y = (155.0/490)*self.x + 480
	    if self.name == "p1":
	    	y = (-150.0/490)*self.x + 650
	    if self.y > y: # reaches the bottom
	        self.down = False
	        self.vy = -23 # velocity reset
	        self.onPlate = False
	        p2.up = True
	    if self.down == False:
	        boing.play()  # sound effects
	        if self.name == "p1":
	        	seesaw.moveLeft = True
	        if self.name == "p2":
	        	seesaw.moveRight = True


	def bounceUp(self, chop):
	    # Bouncing up.
	    self.y  += self.vy
	    self.vy += GRAV
	    prect   = Rect(self.x, self.y, 50, 50)
	    if chop.colliderect(prect) and self.vy > 0:
	        self.y  = 100
	        self.up = False
	        self.vy = -5
	        self.onPlate = True

	def move(self):
		# Allows the player to move left or right.
		keys = key.get_pressed()
		if keys[K_LEFT] and (self.x > self.left_bound):
			self.x -= 5
		if keys[K_RIGHT] and (self.x < self.right_bound):
		    self.x += 5
