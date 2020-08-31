from enum import Enum

class Terreno(Enum):
	AREIA = 1
	AGUA = 2
	TERRA = 3
	BARREIRA = 4
	INICIAL = 5
	FINAL = 6

class Ponto:
	x: int
	y: int
	terreno: Terreno
	
	def __init__(self, x, y, terreno):
		self.x = x
		self.y = y
		self.terreno = terreno

