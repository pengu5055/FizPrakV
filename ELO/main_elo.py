import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr
from scipy.optimize import curve_fit


def linear(x, k, n):
    return k*x + n


c1, c2, c3 = cmr.take_cmap_colors("cmr.bubblegum", 3, cmap_range=(0.3, 1), return_fmt="hex")
d1, d2, d3 = cmr.take_cmap_colors("cmr.cosmic", 3, cmap_range=(0.35, 1), return_fmt="hex")

data1 = np.column_stack(np.genfromtxt("data1.csv", delimiter=",", skip_header=1))
u1 = data1[0]
u1_err = [0.01*i for i in u1]
x1 = data1[1]
x1_err = [0.01*i for i in x1]
y1 = data1[2]
y1_err = [0.01*i for i in y1]

fitpar1, fitcov1 = curve_fit(linear, u1, x1)
fitpar2, fitcov2 = curve_fit(linear, u1, y1)

fit1 = linear(u1, fitpar1[0], fitpar1[1])
fit2 = linear(u1, fitpar2[0], fitpar2[1])

# Plot
# fig, ax = plt.subplots()
# fittext1= "Linear fit: $y = kx + n$\n$k$ =  {} ± {}\n$n$ = {} ± {}"\
#     .format(format(fitpar1[0], ".4e"), format(fitcov1[0][0]**0.5, ".4e"),
#             format(fitpar1[1], ".4e"), format(fitcov1[1][1]**0.5, ".4e"))
# plt.text(0.54, 0.55, fittext1, ha="left", va="center", size=10, transform=ax.transAxes,
#          bbox=dict(facecolor=c3, alpha=0.5))
#
# fittext2= "Linear fit: $y = kx + n$\n$k$ = {} ± {}\n$n$ = {} ± {}"\
#     .format(format(fitpar2[0], ".4e"), format(fitcov2[0][0]**0.5, ".4e"),
#             format(fitpar2[1], ".4e"), format(fitcov2[1][1]**0.5, ".4e"))
# plt.text(0.54, 0.35, fittext2, ha="left", va="center", size=10, transform=ax.transAxes,
#          bbox=dict(facecolor=c2, alpha=0.5))
#
# plt.errorbar(u1, x1, yerr=x1_err,  markersize=2, color=d1,
#              linestyle='None', marker="o", capsize=2, alpha=1, label="X")  # TODO: Determine katera komponenta je to 0 ali 90
# plt.errorbar(u1, y1, yerr=y1_err,  markersize=2, color=d2,
#              linestyle='None', marker="o", capsize=2, alpha=1, label="Y")
# plt.plot(u1, fit1, c=c3)
# plt.plot(u1, fit2, c=c2)
# plt.legend()
#
# plt.title("Sorazmernost odziva z modulacijo")
# plt.xlabel(r"$U_s$ [V]")
# plt.ylabel("[V]")
# plt.show()

# ----- Second Part -----
data2 = np.column_stack(np.genfromtxt("data2.csv", delimiter=",", skip_header=1))

f2 = data2[0]
x2 = data2[1]
x2_err = [0.01*i for i in x2]
y2 = data2[2]
y2_err = [0.01*i for i in y2]

plt.errorbar(f2, x2, yerr=x2_err,  markersize=2, color=d2,
             linestyle='None', marker="o", capsize=2, alpha=1, label="Y")
plt.errorbar(f2, y2, yerr=y2_err,  markersize=2, color=d3,
             linestyle='None', marker="o", capsize=2, alpha=1, label="Y")
plt.show()
