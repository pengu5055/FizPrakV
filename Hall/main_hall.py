import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear(x, k, n):
    return k*x + n


T = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[0])
I = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[5])
U = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[6])
R = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[7])

# Plot R(T)  # TODO: Check da je to res pravilna upornost
fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(linear, xdata=T, ydata=R)
yfit = linear(T, fitpar[0], fitpar[1])
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                     format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.05, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.title("Upornost v odvisnosti od temperature")
plt.xlabel("T [°C]")
plt.ylabel(r"R [$\Omega$]")
plt.plot(T, yfit, color="#A96DA3", label="Linear fit")
plt.errorbar(T, R, yerr=0.1,  markersize=3, color="#27b7f5", linestyle='None', marker="o", capsize=2, label=r"Data", alpha=1)
plt.legend()
plt.show()

# Plot R_H (T)
c = 0.95  # mm
c = c * 10**-3
B = 0.173  # T
R_H = U*c/(I*B)

fitpar, fitcov = curve_fit(linear, xdata=T, ydata=R_H)
yfit = linear(T, fitpar[0], fitpar[1])
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                     format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.05, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.title("Upornost v odvisnosti od temperature")
plt.xlabel("T [°C]")
plt.ylabel(r"$R_H$ [1/(As $m^3$)]")
plt.plot(T, yfit, color="#A96DA3", label="Linear fit")
plt.errorbar(T, R_H, yerr=0,  markersize=3, color="#27b7f5", linestyle='None', marker="o", capsize=2, label=r"Data", alpha=1)
plt.legend()
plt.show()