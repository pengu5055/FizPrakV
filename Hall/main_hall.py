import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear(x, k, n):
    return k*x + n


T = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[0])
I = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[5])
I1 = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[1])
I2 = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[2])
U1 = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[3])
U2 = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[4])
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

# Plot ln(n_p)(1/kT)
k = 1.38 * 10**-23
c = 0.00095
e_0 = -1.6 * 10**-19
T_kelvin = T + 273
xdata = 1/((k*T_kelvin)/np.abs(e_0))
ydata = -(I * B)/(U * c * e_0)  # TODO: The fuck je ta minus tuki
print(ydata)
print(np.log(ydata))
plt.plot(xdata, np.log(ydata), color="#A96DA3")
plt.title(r"$\ln{n}$ v odvisnosti od $\frac{1}{k_B T}$")
plt.xlabel(r"$(eV)^{-1}$")
plt.ylabel(r"$\ln{n}$")
plt.show()

# Dual plot R_1(T)/R_2(T)
fig, (ax1, ax2) = plt.subplots(1, 2)
R1 = U1/I1
R2 = U2/I2
plt.suptitle("Ohmska upornost v odvisnosti od temperature")
ax1.plot(T, R1, color="#1B998B")
ax1.set_title(r"$R_1(T)$")
ax1.set_xlabel(r"T [°C]")
ax1.set_ylabel(r"R [$\Omega$]")
ax2.plot(T, R2, color="#ED217C")
ax2.set_title(r"$R_2(T)$")
ax2.yaxis.tick_right()
ax2.set_xlabel(r"T [°C]")
ax2.set_ylabel(r"R [$\Omega$]")
plt.show()
