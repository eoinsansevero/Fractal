#sierpyr.py

import numpy as np
import matplotlib.pyplot as plt
import random
import itertools as it

from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D


maxX = 1000
maxY = 1000
maxZ = 1000

num_anchors = 5 # pyramid corners
height = 50

# anchor points for triangle (base points in the xy plane)
A = [50, 50, 0]
B = [50, 100, 0]
C = [100, 100, 0]
D = [100, 50, 0]
E = [np.mean([A[0], B[0], C[0], D[0]]), np.mean([A[1], B[1], C[1], D[1]]), height]

anchor_dict = {1:A, 2:B, 3:C, 4:D, 5:E}

x_vals = [A[0], B[0], C[0], D[0], E[0]]
y_vals = [A[1], B[1], C[1], D[1], E[1]]
z_vals = [A[2], B[2], C[2], D[2], E[2]]


# Lets suppose for now that the initial point is one of the 3 anchors --> chosen at random.
START = anchor_dict[random.randint(1, num_anchors)]

updt = it.count()

def update(self):

	# updating function that chooses one of the anchor points
	# at random and creates the next data point that is half-
	# way between the current data point and that anchor.

	if next(updt) == 0:
		point = START
	else:
		point = np.loadtxt("prev_point.txt")

	rand_anchor = anchor_dict[random.randint(1, num_anchors)]

	midpoint = [(point[0] + rand_anchor[0])/2, (point[1] + rand_anchor[1])/2, (point[2] + rand_anchor[2])/2]

	x_vals.append(midpoint[0])
	y_vals.append(midpoint[1])
	z_vals.append(midpoint[2])

	ax.cla()
	ax.scatter(x_vals, y_vals, z_vals, s=1.0)

	np.savetxt("prev_point.txt", midpoint)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = FuncAnimation(plt.gcf(), update, interval=10)

plt.show()

# plt.scatter(x_vals, y_vals, marker='x')
# plt.show()





# count = 0
# while count < 20:
# 	print(int(random.uniform(1, num_anchors + 1)))
# 	count += 1
