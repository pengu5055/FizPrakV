import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr

c1, c2, c3 = cmr.take_cmap_colors("cmr.gem", 3, cmap_range=(0, 1), return_fmt="hex")

# Calibration curve
plt.plot([100, 300, 500], [10, 9, 8], c=c2)
plt.scatter(414, 8.43, c=c3, label="Meritev")
plt.scatter([100, 300, 500], [10, 9, 8], c=c1)
plt.title("Umeritvena krivulja")
plt.xlabel("Lega vijaka")
plt.ylabel(r"$\nu$ [GHz]")
plt.legend()
plt.show()


mer1 = np.column_stack(np.genfromtxt("mer1.csv", delimiter=",", skip_header=2))
x1 = mer1[1]
y1 = mer1[2]
plt.plot(x1, y1)
plt.show()

mer2 = np.column_stack(np.genfromtxt("mer2.csv", delimiter=",", skip_header=2))
x2 = mer2[1]
y2 = mer2[2]
plt.plot(x2, y2)
plt.show()

mer3 = np.column_stack(np.genfromtxt("mer3.csv", delimiter=",", skip_header=2))
x3 = mer3[1]
y3 = mer3[2]
plt.plot(x3, y3)
plt.show()
