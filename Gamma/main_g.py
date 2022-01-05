import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr


def square(x, a, b, c):
    """Second order polynomial"""
    return a*x**2 + b*x + c


c1, c2, c3 = cmr.take_cmap_colors("cmr.cosmic", 3, cmap_range=(0.3, 1), return_fmt="hex")

# Calibration data
a = 3.43568e-015
b = 0.000763955
c = 3.01129e-008




# Hand measured plot
# data1 = np.column_stack(np.genfromtxt("Na22_counterdata.csv", delimiter=",", skip_header=1))
# windows, rates = data1
#
# plt.bar(windows, rates, width=0.5, color=c1)
#
# plt.title(r"$^{22}\mathrm{Na}$ spekter pomerjen ročno")
# plt.xlabel("Lower level")
# plt.ylabel(r"R [$s^{-1}$]")
# plt.show()

# Draw calibrated plot
data2 = np.column_stack(np.genfromtxt("Na22_calib.txt", skip_header=20))
x_uncalib = data2[0]
energy = square(x_uncalib, a, b, c)
y = data2[1]
plt.bar(energy, y, color=c1, width=(energy[1] - energy[0]))
plt.show()
