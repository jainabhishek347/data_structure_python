class Graph(object):
	def __init__(self, graph=None):
		if graph is  None:
			self.graph_dict = []
		else:
			self.graph_dict = graph

	def find_route(self, ver1, ver2, path=None):
		if path == None:
			path = []
		path.append(ver1)
		if ver1== ver2:
			return path		
		if ver1 in self.graph_dict:
			for edges in self.graph_dict[ver1]:
				if edges not in path:
					e_path = self.find_route(edges, ver2, path)
					if e_path:
						return e_path
		return None

graph = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

g = Graph(graph)
print g.find_route("a", "b")