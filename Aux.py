from enum import Enum

class Terreno(Enum):
	INICIO = 0
	TERRA = 1
	AGUA = 2
	AREIA = 3
	BARREIRA = 4
	FINAL = 5

class Ponto:
	x: int
	y: int
	terreno: Terreno
	
	def __init__(self, x, y, terreno):
		self.x = x
		self.y = y
		self.terreno = terreno

