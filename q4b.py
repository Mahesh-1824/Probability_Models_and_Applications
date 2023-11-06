import numpy as np

probability_matrix = [[1/4, 1/2, 1/4],
                    [1/3, 0, 2/3],
                    [1/2, 0, 1/2]]

start_dist = [1, 0, 0]

num_of_steps = 100

for _ in range(num_of_steps):
    start_dist = np.dot(start_dist, probability_matrix)

limiting_dist = start_dist / np.sum(start_dist)

print("Limiting Distribution for the Markov chain is :", limiting_dist)
