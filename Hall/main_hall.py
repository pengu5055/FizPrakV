import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear(x, k, n):
    return k*x + n


T = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[0])
I = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[5])
U = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[6])
R = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[7])


fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(linear, xdata=T, ydata=R)
yfit = linear(T, fitpar[0], fitpar[1])
fittext= "Linear fit: $y = kx + n$\nk = {} ± {}\nn = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                     format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.05, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
plt.title("Upornost v odvisnosti od temperature")
plt.xlabel("T [°C]")
plt.ylabel(r"R [$\Omega$]")
plt.plot(T, yfit)
plt.errorbar(T, R, yerr=0.1)
plt.show()
