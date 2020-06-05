import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

ax3d = plt.figure().gca(projection='3d')

arrayx = np.array([[0.7], [7.1], [7.5], [0.6], [0.5], [0.00016775708773695687]])
arrayy = np.array([[0.1], [2], [3], [6], [5], [16775708773695687]])
arrayz = np.array([[1], [2], [3], [4], [5], [6]])

labels = ['one', 'two', 'three', 'four', 'five', 'six']

arrayx = arrayx.flatten()
arrayy = arrayy.flatten()
arrayz = arrayz.flatten()

ax3d.scatter(arrayx, arrayy, arrayz)

#give the labels to each point
for x_label, y_label, z_label, label in zip(arrayx, arrayy, arrayz, labels):
    ax3d.text(x_label, y_label, z_label, label)

plt.title("Data")
plt.show()
