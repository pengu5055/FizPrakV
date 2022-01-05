import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr
from scipy.optimize import curve_fit


def square(x, a, b, c):
    """Second order polynomial"""
    return a*x**2 + b*x + c


def exp(x, C, k):
    return C * np.exp(-k*x)


def linear(x, k, n):
    return k*x + n


c1, c2, c3 = cmr.take_cmap_colors("cmr.cosmic", 3, cmap_range=(0.3, 1), return_fmt="hex")

# Square calibration data
a = 3.43568e-015
b = 0.000763955
c = 3.01129e-008


# Background data
bg_tmes = 100
bg1 = np.column_stack(np.genfromtxt("bg1.txt", skip_header=15))
bg2 = np.column_stack(np.genfromtxt("bg2.txt", skip_header=15))
bg3 = np.column_stack(np.genfromtxt("bg3.txt", skip_header=15))
bg = (bg1 + bg2 + bg3)/3
bg_x = bg[0]
bg_scaled = square(bg_x, a, b, c)
bg_y = bg[1] / bg_tmes
lag = 85  # How many elements to skip at the beginning of fit
fitpar, fitcov = curve_fit(exp, bg_scaled[lag:], bg_y[lag:], p0=[0.7, 6])
bg_fit = exp(bg_scaled[lag:], fitpar[0], fitpar[1])

fig, ax = plt.subplots()
fittext= "Exponential fit: $y = Cexp(-kx)$\n$C$ = {} ± {}\n$k$ = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                                 format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.55, 0.9, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor=c3, alpha=0.5))

plt.plot(bg_scaled, bg_y, c=c1)
plt.plot(bg_scaled[lag:], bg_fit, c=c3)

plt.title("Šum ozadja")
plt.xlabel("E [MeV]")
plt.ylabel(r"R [$s^{-1}$]")
plt.show()
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

# Draw calibrated plot Na22
data2_tmes = 50
data2 = np.column_stack(np.genfromtxt("Na22_calib.txt", skip_header=20))
x_uncalib = data2[0]
energy = square(x_uncalib, a, b, c)
y = data2[1]/data2_tmes - bg_y[:len(data2[1])]
plt.bar(energy, y, color=c1, width=(energy[1] - energy[0]))

plt.title(r"$^{22}\mathrm{Na}$ spekter brez ozadja")
plt.xlabel("E [MeV]")
plt.ylabel(r"R [$s^{-1}$]")
plt.show()

# Draw Co60 plot
data3_tmes = 50
data3 = np.column_stack(np.genfromtxt("co60.txt", skip_header=6))
x_uncalib = data3[0]
energy = square(x_uncalib, a, b, c)
y = data3[1]/data3_tmes - bg_y[:len(data3[1])]
plt.bar(energy, y, color=c1, width=(energy[1] - energy[0]))

plt.title(r"$^{60}\mathrm{Co}$ spekter brez ozadja")
plt.xlabel("E [MeV]")
plt.ylabel(r"R [$s^{-1}$]")
plt.show()

# Draw Cs137 plot
data4_tmes = 50
data4 = np.column_stack(np.genfromtxt("cs137.txt", skip_header=6))
x_uncalib = data4[0]
energy = square(x_uncalib, a, b, c)
y = data4[1]/data4_tmes - bg_y[:len(data4[1])]
plt.bar(energy, y, color=c1, width=(energy[1] - energy[0]))

plt.title(r"$^{137}\mathrm{Cs}$ spekter brez ozadja")
plt.xlabel("E [MeV]")
plt.ylabel(r"R [$s^{-1}$]")
plt.show()
