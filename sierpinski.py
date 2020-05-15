#sierpinski.py

import numpy as np
import matplotlib.pyplot as plt
import random
import itertools as it

from matplotlib.animation import FuncAnimation

eoin = 10
equalateral_mode = False


maxX = 1000
maxY = 1000

num_anchors = 3 # i.e. a triangle

# anchor points for triangle
A = [int(random.uniform(1, maxX+1)), int(random.uniform(1, maxY+1))]
B = [int(random.uniform(1, maxX+1)), int(random.uniform(1, maxY+1))]
C = [int(random.uniform(1, maxX+1)), int(random.uniform(1, maxY+1))]

anchor_dict = {1:A, 2:B, 3:C}

x_vals = [A[0], B[0], C[0]]
y_vals = [A[1], B[1], C[1]]

# # Impose the condition that the initial point is bounded inside the triangle
# init_x = random.uniform(min(x_vals), max(x_vals))
# base_length = np.sqrt((x1-x2)**2 + (y1-y2)**2)

# ^^ implement in the future
# Lets suppose for now that the initial point is one of the 3 anchors --> chosen at random.
START = anchor_dict[int(random.uniform(1, num_anchors+1))]

updt = it.count()

def update(self):

	# updating function that chooses one of the anchor points
	# at random and creates the next data point that is half-
	# way between the current data point and that anchor. 

	if next(updt) == 0:
		point = START
	else:
		point = np.loadtxt("prev_point.txt")

	rand_anchor = anchor_dict[int(random.uniform(1, num_anchors+1))]

	midpoint = [(point[0] + rand_anchor[0])/2, (point[1] + rand_anchor[1])/2]

	x_vals.append(midpoint[0])
	y_vals.append(midpoint[1])

	plt.cla()
	plt.scatter(x_vals, y_vals, s=1)	

	np.savetxt("prev_point.txt", midpoint)

	


ani = FuncAnimation(plt.gcf(), update, interval=10)

plt.show()

# plt.scatter(x_vals, y_vals, marker='x')
# plt.show()





# count = 0
# while count < 20:
# 	print(int(random.uniform(1, num_anchors + 1)))
# 	count += 1 


