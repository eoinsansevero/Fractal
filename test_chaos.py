#test_chaos.py

import matplotlib.pyplot as plt
import numpy as np
import random
import itertools as it


integers = np.array(range(1000))

for i in integers:
	integers[i] = int(random.uniform(1,4))

print(integers)
counts, bins = np.histogram(integers, bins=3)
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, counts)
plt.show()
