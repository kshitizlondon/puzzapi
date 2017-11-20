class GraphNode():
	def __init__(self, data, directed):
		self.data = data
		self.adj = [] #of node ids
		self.directed = directed


class Graph():
	def __init__(self, V, E, type):
		self.V = V
		self.E = E
		self.type = graph_type
		self.vmap = {}

	def getVertexFromId(self, id):
		return self.vmap[id]

	def getGraphType(self):
		return self.type

	


