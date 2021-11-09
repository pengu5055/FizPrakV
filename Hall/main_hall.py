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
Ed = 0.01  # eV
Eg = 0.66  # eV

fig, ax = plt.subplots()
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
plt.title("Hallova konstanta v odvisnosti od temperature")
plt.xlabel("T [°C]")
plt.ylabel(r"$R_H$ [$m^3$/As]")
plt.plot(T, yfit, color="#A96DA3", label="Linear fit")
y_err = [0.005 * element for element in R_H]
plt.errorbar(T, R_H, yerr=y_err,  markersize=3, color="#27b7f5", linestyle='None', marker="o", capsize=2, label=r"Data", alpha=1)
plt.legend()
plt.show()

# Plot ln(n_p)(1/kT)
k = 1.38 * 10**-23
c = 0.00095
e_0 = -1.6 * 10**-19  # TODO: Al je tut kle minus? Nekaj je wonky
T_kelvin = T + 273
xdata = 1/((k*T_kelvin)/np.abs(e_0))
ydata = -(I * B)/(U * c * e_0)  # TODO: The fuck je ta minus tuki
ed_xdata = xdata[:4]
ed_ydata = ydata[:4]
eg_xdata = xdata[4:]
eg_ydata = ydata[4:]
edfitpar, edfitcov = curve_fit(linear, xdata=ed_xdata, ydata=np.log(ed_ydata))
egfitpar, egfitcov = curve_fit(linear, xdata=eg_xdata, ydata=np.log(eg_ydata))
edfit = linear(ed_xdata, edfitpar[0], edfitpar[1])
egfit = linear(eg_xdata, egfitpar[0], egfitpar[1])
plt.plot(xdata, np.log(ydata), color="#A96DA3")
plt.plot(ed_xdata, edfit, label=r"Linear fit 1", ls="-")
plt.plot(eg_xdata, egfit, label=r"$Linear fit 2$", ls="-")
plt.title(r"$\ln{n}$ v odvisnosti od $\frac{1}{k_B T}$")
plt.xlabel(r"$(eV)^{-1}$")
plt.ylabel(r"$\ln{n}$")
plt.legend()
plt.show()

# Dual plot R_1(T)/R_2(T)
fig, (ax1, ax2) = plt.subplots(1, 2)
R1 = U1/I1
R2 = U2/I2
plt.suptitle("Ohmska upornost v odvisnosti od temperature")
ax1.plot(T, R1, color="#1B998B", label=r"$R_1 = \frac{U_1}{I_1}$")
ax1.set_title(r"$R_1(T)$")
ax1.set_xlabel(r"T [°C]")
ax1.set_ylabel(r"R [$\Omega$]")
ax1.legend()
ax2.plot(T, R2, color="#ED217C", label=r"$R_2 = \frac{U_2}{I_2}$")
ax2.set_title(r"$R_2(T)$")
ax2.yaxis.tick_right()
ax2.set_xlabel(r"T [°C]")
ax2.set_ylabel(r"R [$\Omega$]")
ax2.legend()

plt.show()
