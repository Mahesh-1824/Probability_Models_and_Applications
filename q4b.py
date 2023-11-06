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


# import numpy as np

# probability_matrix = [[1/4, 1/2, 1/4],
#                     [1/3, 0, 2/3],
#                     [1/2, 0, 1/2]]

# start_state = 0
# start_dist = [0, 0, 0]
# start_dist[start_state] = 1
# prev_state = start_state
# num_of_steps = 100
# i=0
# while i<num_of_steps:
#     curr_state = np.random.choice([0,1,2],p=probability_matrix[prev_state])
#     start_dist[curr_state]+=1
#     prev_state=curr_state
#     i += 1
# # for _ in range(num_of_steps):
# #     start_dist = np.dot(start_dist, probability_matrix)

# limiting_dist = start_dist / np.sum(start_dist)

# print("Limiting Distribution for the Markov chain is :", limiting_dist)
