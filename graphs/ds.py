class GraphVertex():
	def __init__(self, data):
		self.id = None
		self.data = data
		
		self.adj = []
		self.inc = None
		self.out = None
		

class GraphEdge():
	def __init__(self, source, destination, weight=1, weighted):
		self.src = source
		self.dest = destination

		if weighted == True:
			self.weight = data
		else:
			self.weight = 1


class Graph():
	def __init__(self, V, E, type):
		self.V = V
		self.E = E
		self.init_graph()

		self.type = graph_type
		self.vmap = {}

	def init_graph(self):
		i = 0
		for v in V:
			self.vmap[i] = v
			v.id = i
			i+=1

		for e in E:
			v_src = e.src
			v_dest = e.dest



	def getVertexFromId(self, id):
		return self.vmap[id]

	def getGraphType(self):
		return self.type

	


