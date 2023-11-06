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
B = np.ones(8)
A = np.eye(8)
for i in range(8):
    for j in range(8):
        if probability_matrix[i][j] != 0 and j != 7:
            A[i][j] = -probability_matrix[i][j]
x = np.linalg.solve(A, B)

print("The number of steps taken is  " + str(math.ceil(x[0])))
