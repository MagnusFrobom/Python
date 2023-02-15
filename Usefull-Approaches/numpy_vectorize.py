'''  Instead of using a for loop

def euclidean_distance(x, y):
    distance = np.empty(x.shape)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            distance[i, j] = np.sqrt((x[i, j] - y[I, j])**2)
    return distance
'''

import numpy as np

def euclidean_distance(x, y):
    return np.sqrt((x - y)**2)

vectorized_distance =np.vectorize(euclidean_distance)

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[2, 3, 4], [5, 6, 7]])

result = vectorized_distance(x, y)
