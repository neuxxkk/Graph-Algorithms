import string

class Node():
	def __init__(self, tag, parent = None, distance = float('inf')):
		self.tag = tag
		self.parent = parent
		self.distance = distance
	
	def __lt__(self, n):
		return self.distance < n.distance	

	def __str__(self):
		return f"{self.tag} - {string.ascii_lowercase[self.tag]} pai: {self.parent}, distance: {self.distance}"

class BellmanFord():
	def __init__(self, source, numVertices, graph = None, edges = None, adjMatrix = None):
		self.graph = graph
		self.adjMatrix = adjMatrix
		self.edges = edges
		self.numVertices = numVertices
		self.source = source
		if (graph): self.alg_edges()
		elif (adjMatrix): self.adj_matrix()

	def adj_matrix(self):
		distances = [float('inf')] * self.numVertices
		parents = [None] * self.numVertices
		parents[source] = -1
		distances[source] = 0

		for __ in range(self.numVertices - 1):
			for i in range(self.numVertices):
				for j in range(self.numVertices):
					if adjMatrix[i][j] != 0:
						newDist = distances[i] + adjMatrix[i][j]
						if newDist < distances[j]:
							distances[j] = newDist
							parents[j] = i

		for v in range(numVertices):
			print(f'{v} - {string.ascii_lowercase[v]} pai: {parents[v]}, distance: {distances[v]}')

		for i in range(self.numVertices):
			for j in range(self.numVertices):
				if adjMatrix[i][j] != 0:
					newDist = distances[i] + adjMatrix[i][j]
					if newDist < distances[j]:
						print("Ciclo negativo!")
						return False

	def alg_edges(self):
		for __ in range(numVertices - 1):
			for e in edges:
				self.relax(e)
		
		for n in graph: print(n)

		for e in edges:
			if graph[e[0]].distance + edges[e] < graph[e[1]].distance: # aresta não relaxada -> ciclo negativo>infinito
				print("Ciclo negativo!")
				return False # sem solução
		

	def relax(self, edge):
		src = edge[0]
		dest = edge[1] # possible new Distance
		weight = self.edges[edge]
		newDist = self.graph[src].distance + weight
		if newDist < graph[dest].distance:
			graph[dest].distance = newDist
			graph[dest].parent = src


# initializating
adjMatrix = [
   # A  B  C
    [0, 5, 4],  # A
    [1, 0, 0],  # B
    [0, -3, 0],  # C
]

numVertices = len(adjMatrix)
edges = {}
graph = []

# matrizAdj -> edge list
for i in range(numVertices):
	for j in range(numVertices):
		if adjMatrix[i][j] != 0: edges[(i, j)] = adjMatrix[i][j]

source = 0 # A

# creating graph of Nodes()
for i in range(numVertices):
	graph.append(Node(i, -1, 0) if i == source else Node(i))

print(edges)

bf = BellmanFord(source, len(adjMatrix), adjMatrix = adjMatrix)
