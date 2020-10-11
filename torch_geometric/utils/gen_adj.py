from math import sqrt

def calcEuclDistance(x1, y1, x2, y2):
	'''
		Calculates the Euclidean distance given the coordinates
		of two points.
	'''
	return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def generateAdjMatrix(obs, radius):
	'''
		Generates the adjacency matrix of a graph.

		Input:

		obs: V x F 2D array
			 V: number of vehicles
			 F: number of features (assuming "presence", "x", "y")

		radius: determines minimum distance between vehicles 
		for them to be considered neighbors
	'''
	num_vehicles = len(obs)
	adj = np.zeros((num_vehicles, num_vehicles))
	for i in range(num_vehicles):
		for j in range(i + 1, num_vehicles):
			if calcEuclDistance(obs[i][1], obs[i][2], obs[j][1], obs[j][2]) <= radius:
				if obs[i][0] != 0 and obs[j][0] != 0:
					adj[i][j], adj[j][i] = 1, 1
	return adj
