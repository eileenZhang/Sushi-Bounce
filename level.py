
from pygame import *
from fruits import Fruit

possibleScore = [0, 1,  2,  3,  4,  5,  6,  7,  8,  9,  10,11,12,13,14,15,-5,-5,18,20,10,0,0,0,0,0,0]

le = [[""],["rice","seaweed","caviar"],
		["rice","seaweed","vinegar","cucumber"],
		["rice","seaweed","vinegar","wasabi","salmon"],
		["vinegar","sugar","salt","caviar"],
		["rice","seaweed","vinegar","cucumber","avocado","sesame","soysauce","crabmeat"],
		["rice","seaweed","carrot","avocado","scallion","crabmeat","ginger","unagi","wasabi","shrimp"]]

ocurrence = [ [0],
			  [0, 400, 400, 100, 50,  50,  50,  50, 50, 50,  400,10,  10, 5,  5,   10, 300, 300, 5,  5, 3,  50,50,50,50,50,50],
			  [0, 400, 400, 400, 100, 100, 150, 400,50, 50,  20, 200, 12, 6,  3,   10, 300, 300, 2,  2 ,2,  50,50,50,50,50,50],
			  [0, 400, 400, 400, 100, 100, 150, 50, 50, 50,  20, 300, 300,6,  3,   10, 300, 300, 2,  2 ,2  ,50,50,50,50,50,50],
			  [0, 400, 200, 300, 200, 200, 150, 50, 50, 50,  220,200, 12, 6,  3,   10, 300, 300, 2,  2, 2,  50,50,50,50,50,50],
			  [0, 300, 300, 300, 100, 100, 150, 200,200,50,  20, 200, 12, 200,200, 200,200, 200, 2,  3, 2,  50,50,50,50,50,50],
			  [0, 400, 400, 100, 100, 100, 150, 50, 50, 50,  20, 200, 12, 6,  3,   10, 300, 300, 100,100,100,  50,50,50,50,50,50]]

all_fruits = ["0", 
			  "rice","seaweed","vinegar","sugar","salt","carrot","cucumber",
			  "avocado","scallion","caviar","wasabi","salmon","crabmeat","soysauce",
			  "sesame","lemon","egg", "unagi","ginger","shrimp","INCspeed","DECspeed","+Life","-Life","INCtime","DECtime"]

speical = ["INCspeed","DECspeed","+Life","-Life","INCtime","DECtime"]
all_f = {}
all_f["0"] = "0"                                                    # list of ingredient pictures
for i in range(1,27):
	pic = image.load("ingredient graphics/"+str(i)+"."+".png")
	all_f[all_fruits[i]] = pic

class Level():
	def __init__(self, level):
		self.req = []
		requirements = le[level] 
		for i in le[level]:
			f = Fruit(i, 0, 0, 0, 0, 0, "", all_f[i])
			self.req.append(f)
		self.num = level
		self.fruitsList = []
		for i in range(len(all_fruits)):
			if all_fruits[i] in speical:
				s = all_fruits[i]
			else:
				s = ""
			f = Fruit(all_fruits[i], 0, 0, possibleScore[i], 0, 0, s, pics[all_fruits[i]])
			for j in range(ocurrence[level][i]):
				self.fruitsList.append(f)
