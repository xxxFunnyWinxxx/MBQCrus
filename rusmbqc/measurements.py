import numpy as np
from constants import *

class BaseMeas:
	def __init__(self):
		self.basis = None
		self.name = None
		

class Z(BaseMeas):
	def __init__(self):
		self.basis = Z_basis
		self.name = 'Z'
		
class X(BaseMeas):
	def __init__(self):
		self.basis = X_basis
		self.name = 'X'
		
class Y(BaseMeas):
	def __init__(self):
		self.basis = Y_basis
		self.name = 'Y'
		
class X_Y(BaseMeas):
	def __init__(self, alpha: float):
		self.basis = 0.5 ** (1/2) * np.array([[np.exp(1j*alpha), np.exp(-1j*alpha)],
											[np.exp(1j*alpha), -np.exp(-1j*alpha)]])
		self.name = f'X_Y({alpha})'
