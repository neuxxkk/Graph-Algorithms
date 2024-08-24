import heapq

adjList = {
	'A':[1,2,3,5,6,7], # A - 0
	'B':[0,4,5],	   # B - 1
	'C':[0,3],	       # C - 2
	'D':[0,2,4],       # D - 3
	'E':[1,3],	       # E - 4
	'F':[0,1,7],       # F - 5
	'G':[0,7],         # G - 6
	'H':[0,5,6]	       # H - 7
}

adjMatrix = [
    [0, 2, 3, 4, 0, 1, 7, 8],  # A
    [2, 0, 0, 0, 5, 7, 0, 0],  # B
    [3, 0, 0, 8, 0, 0, 0, 0],  # C
    [4, 0, 8, 0, 3, 0, 0, 0],  # D
    [0, 5, 0, 3, 0, 0, 0, 0],  # E
    [1, 7, 0, 0, 0, 0, 0, 4],  # F
    [7, 0, 0, 0, 0, 0, 0, 5],  # G
    [8, 0, 0, 0, 0, 4, 5, 0]   # H
]

numVertices = len(adjMatrix)

edges = {}

# matrizAdj -> edge list
for i in range(numVertices):
	for j in range(numVertices):
		if adjMatrix[i][j] != 0: edges[(i, j)] = adjMatrix[i][j]


class Djistraka():
	def __init__(self, G, numVertices):
		self.G = G
		self.numVertices = numVertices
		self.distances = [float('inf')] * self.numVertices	
		self.parents = [None] * self.numVertices
		self.visited = [False] * self.numVertices
		self.mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
		
	def set(self, start, goal):
		self.start = self.mapping[start]
		self.goal = self.mapping[goal]
		self.distances[self.start] = 0
		self.parents[self.start] = -1


	def adj_matrix(self, start, goal):
		adjMatrix = self.G
		self.set(start, goal)
		for __ in range(self.numVertices):
			minDist = float('inf')
			current = None
			for i in range(self.numVertices):
				if self.distances[i] < minDist and not self.visited[i]:
					minDist = self.distances[i]
					current = i

			if current is not None:
				self.visited[current] = True
				for v, weight in enumerate(adjMatrix[current]): # for adjancency in...
					if weight:
						newDist = self.distances[current] + weight
						if newDist < self.distances[v]:
							self.distances[v] = newDist
							self.parents[v] = current
		self.show_path()	

	def adj_list(self, start, goal):
		adjList = self.G
		self.set(start, goal)
		for __ in range(self.numVertices):
			minDis = float('inf')
			current = None

			for i in range(self.numVertices):
				if not self.visited[i] and self.distances[i] < minDis:
					minDis = self.distances[i]
					current = i

			if current is not None:
				self.visited[current] = True		
				for v in range(self.numVertices):
					if v in adjList[list(adjList.keys())[current]]:
						newDist = self.distances[current] + 1
						if newDist < self.distances[v]:
							self.parents[v] = current
							self.distances[v] = newDist
		self.show_path()

	def edge_list(self, start, goal):
		edges = self.G
		self.set(start, goal)

		for __ in range(self.numVertices):
			current = None
			minDis = float('inf')

			for v in range(self.numVertices):
				if self.distances[v] < minDis and not self.visited[v]:
					current = v
					minDis = self.distances[v]

			if current is not None:
				self.visited[current] = True
				for e in edges:
					if e[0] == current:
						newDist = self.distances[e[0]] + edges[e]
						if newDist < self.distances[e[1]]:
							self.distances[e[1]] = newDist
							self.parents[e[1]] = current
		self.show_path()

	def show_path(self):
	    path = []
	    v = self.goal
	    while v != -1:
	        atual = list(self.mapping.keys())[v]
	        path.append(atual)
	        v = self.parents[v]
	    
	    path.reverse()

	    for i, v in enumerate(path):
	        print(v, end=' --> ' if i < len(path) - 1 else '\n')



d = Djistraka(edges, numVertices)

d.edge_list('H', 'E')