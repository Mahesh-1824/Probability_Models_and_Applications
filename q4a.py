import numpy as np 
import random
import math
probability_matrix = [[0,1/3,1/3,1/3,0,0,0,0],
                      [1/3,0,0,0,1/3,0,1/3,0],
                      [1/3,0,0,0,0,1/3,1/3,0],
                      [1/3,0,0,0,1/3,1/3,0,0],
                      [0,1/3,0,1/3,0,0,0,1/3],
                      [0,0,1/3,1/3,0,0,0,1/3],
                      [0,1/3,1/3,0,0,0,0,1/3],
                      [0,0,0,0,0,0,0,1]]
sum_of_prob = np.ones(8)
prob = np.eye(8)
for i in range(8):
    for j in range(8):
        if probability_matrix[i][j] != 0 and j != 7:
            prob[i][j] = -probability_matrix[i][j]
times = np.linalg.solve(prob, sum_of_prob)

print("The number of steps taken is  " + str(math.ceil(times[0])))
