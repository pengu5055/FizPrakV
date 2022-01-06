import numpy as np
import matplotlib.pyplot as plt

data1 = np.column_stack(np.genfromtxt("data1.csv", delimiter=",", skip_header=1))
u1 = data1[0]
x1 = data1[1]
y1 = data1[2]
plt.plot(u1, y1)
plt.show()
