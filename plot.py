import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt('points.csv', delimiter=',')

x_max = np.max(points[:, 0])
x_min = np.min(points[:, 0])
y_max = np.max(points[:, 1])
y_min = np.min(points[:, 1])

guess_centroids = np.random.randint([x_min, y_min], [x_max, y_max], size=(4, 2))
print(guess_centroids)
print(x_min, x_max, y_min, y_max)
plt.scatter(points[:, 0], points[:, 1], color='blue')

def get_dist(x, y):
    return np.sqrt(x**2 + y**2)

def assign_points():
    

def k_means_algo():
    
# plt.scatter(guess_centroids[:, 0], guess_centroids[:, 1], color='red')
plt.show()

# End of file
