import numpy as np
import networkx as nx

class Frame:
	def __init__(self, set_of_meas: dict = None):
		if set_of_meas == None:
			self.set_of_meas = {}
		else:
			self.set_of_meas = set_of_meas
		
	def append(self, node, meas):
		if node in self.nodes():
			print(f'Node {node} already determined')
		else:
			self.set_of_meas[node] = meas
		
	def nodes(self):
		return self.set_of_meas.keys()
		
	def meas(self, node):
		return self.set_of_meas[node]
	
