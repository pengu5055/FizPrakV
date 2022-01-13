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


# mer1 = np.column_stack(np.genfromtxt("mer1.csv", delimiter=",", skip_header=2))
# x1 = mer1[1]
# y1 = mer1[2]
# plt.scatter(x1, y1, s=3, c=c1)
# plt.show()

mer2 = np.column_stack(np.genfromtxt("mer2.csv", delimiter=",", skip_header=2))
x2 = mer2[1]
y2 = mer2[2]
plt.scatter(x2, y2, s=3, c=c2, label="Kratkostična stena")

plt.title("Krivulja ubranosti z kratkostično steno")
plt.xlabel("Razdalja [cm]")
plt.ylabel("Signal [V]")
# plt.show()

mer3 = np.column_stack(np.genfromtxt("mer3.csv", delimiter=",", skip_header=2))
x3 = mer3[1]
y3 = mer3[2]
plt.scatter(x3, y3, s=3, c=c3, label="Bolometer")

plt.title("Krivulja ubranosti")
plt.xlabel("Razdalja [cm]")
plt.ylabel("Signal [V]")
plt.legend()
plt.show()


def reak(s, b):
    return ((s**2 - 1) * np.tan(b))/(1 + s**2 * (np.tan(b))**2)


print(reak(0.66, 2.74), reak(0.66, 2.74) * 0.07)


def rez(s, b):
    return (1 - reak(s, b) * np.tan(b))*s


print(rez(0.66, 2.74), rez(0.66, 2.74) * 0.07)

# Solutions plot
data = np.column_stack(np.genfromtxt("data1.csv", delimiter=",", skip_header=1))
x = data[0]
y = data[1]
y_err = [0.02*i for i in y]
plt.errorbar(x, y, yerr=y_err,  markersize=2, color=c2,
             linestyle='None', marker="o", capsize=2, alpha=1)
plt.plot(x, y, c=c3, alpha=0.2)

plt.title("Rodovi klistronovega delovanja")
plt.xlabel("U [V]")
plt.ylabel(r"$U_{\mathrm{sig}}$ [mV]")
plt.show()


# Power plot
def to_true_power(p_m, r_R_square):
    return p_m/(1 - r_R_square)


data2 = np.column_stack(np.genfromtxt("power_data.csv", delimiter=",", skip_header=1))
u = data2[0]
p_m = data2[1]
r_R_sq = 0.042
p = to_true_power(p_m, r_R_sq)
p_err = [0.02 * i for i in p]
plt.errorbar(u, p, yerr=p_err,  markersize=2, color=c2,
             linestyle='None', marker="o", capsize=2, alpha=1)
plt.plot(u, p, c=c3, alpha=0.2)

plt.title("Moč rodov")
plt.xlabel("U [V]")
plt.ylabel("P [mW]")
plt.show()
