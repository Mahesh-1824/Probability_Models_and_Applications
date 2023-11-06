import random
import numpy as np
import matplotlib.pyplot as plt

def generate_data(num_points=100):
    A = np.random.random(num_points)
    B = np.random.random(num_points)
    t = np.linspace(0, num_points, num=num_points)
    return A, B, t

def h(T):
    time_stamps = []
    for t in T:
        if t > 0:
            time_stamps.append(np.exp(-t))
        else:
            time_stamps.append(0)
    return time_stamps

if __name__ == "__main__":
    A, B, t = generate_data(100)
    X1=[]
    X2 = []
    for i in t:
        x=np.exp(-(i+A))
        x1=np.exp(np.sin(i+A))
        X2.append(x)
        X1.append(x1)
    X2 = np.array(X2)
    X2 = X2.T
    X1 = np.array(X1)
    X1 = X1.T
    
    Y1 = []
    Y2 = []
    for i in range(X2.shape[1]):
        y1 = np.convolve(X2[i], h(t), mode="full")
        Y1.append(y1)
        y2 = np.convolve(X1[i], h(t), mode="full")
        Y2.append(y2)

    
    mean_list = []
    mean_list2=[]
    Y1 = np.array(Y1)
    Y2 = np.array(Y2)
    for i in range(Y1.shape[0]):
        mean_list.append(np.mean(Y1[i]))
        mean_list2.append(np.mean(Y2[i]))
    mean_list = np.array(mean_list)
    mean_list2 = np.array(mean_list2)
    
    print("MAX mean =", np.max(mean_list), "MIN mean =", np.min(mean_list))
    print("MAX mean =", np.max(mean_list2), "MIN mean =", np.min(mean_list2))
    
    autocorrelation_list = []
    autocorrelation_list2 = []
    for i in range(Y1.shape[0]):
        for j in range(i + 1, Y1.shape[0]):
            autocorrelation_list.append(np.correlate(Y1[i], Y1[j]))
            autocorrelation_list2.append(np.correlate(Y2[i], Y2[j]))
    
    autocorrelation_arr = np.array(autocorrelation_list)
    autocorrelation_arr2 = np.array(autocorrelation_list2)
    print(np.max(autocorrelation_arr), np.min(autocorrelation_arr))
    print(np.max(autocorrelation_arr2), np.min(autocorrelation_arr2))
    
    autocorrelation_matrix = np.zeros((Y1.shape[0], Y1.shape[0]))
    autocorrelation_matrix2 = np.zeros((Y2.shape[0], Y2.shape[0]))
    
    for i in range(Y1.shape[0]):
        for j in range(Y1.shape[0]):
            autocorrelation = np.correlate(Y1[i], Y1[j], mode='full')
            autocorrelation_matrix[i, j] = autocorrelation[len(autocorrelation) // 2]
            autocorrelation2 = np.correlate(Y2[i], Y2[j], mode='full')
            autocorrelation_matrix2[i, j] = autocorrelation2[len(autocorrelation2) // 2]
    
    plt.subplot(1,2,1)
    plt.plot(autocorrelation_arr,label = "Plot1")
    plt.legend()
    plt.subplot(1,2,2)
    plt.plot(autocorrelation_arr2,label="Plot2")
    plt.legend()
    plt.show()
