import numpy as np
import networkx as nx
from constants import *

class Scheme:
	def __init__(self, graph: nx.classes.graph.Graph):
		self.mapping = {node: i for i, node in enumerate(list(graph.nodes))}
		self.graph = nx.relabel_nodes(graph, self.mapping)
		self.num_q = graph.number_of_nodes()
		self.psi = self.create_graph_state()
		
	def create_graph_state(self):
		psi = 0.5 ** (self.num_q/2) * np.ones([2 for _ in range(self.num_q)])
		
		for pair in self.graph.edges:
			psi = np.moveaxis(np.tensordot(psi, CZ_tens, axes = (pair, (0, 1))), (-2, -1), pair)
	
		return psi
		
	def perform_frame(self, frame):
		for node in frame.nodes():
			meas_val = self.measure(node, frame.meas(node))
			print(f'Measurement {frame.meas(node).name} on node {node} : {meas_val}')
		
	
	def measure(self, node, meas):
		psi_meas = np.tensordot(self.psi, meas.basis[0], axes = (self.mapping[node], 0))	
		psi_meas_norm = np.linalg.norm(psi_meas)
		prob = psi_meas_norm ** 2
		if np.random.random() < prob:
			meas_val = 0
		else:
			meas_val = 1
		
		self.psi = psi_meas / psi_meas_norm
		self.update_map(node)
		
		return meas_val
	
	
	def update_map(self, node_to_del):
		k = self.mapping[node_to_del]
		del self.mapping[node_to_del]
		for key in self.mapping:
			if self.mapping[key] > k:
				self.mapping[key] -= 1
		self.num_q -= 1
		
		
	def left_psi(self):
		return self.psi.reshape(2 ** self.num_q)
		

