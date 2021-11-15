import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear(x, k, n):
    return k*x + n


T = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[0])
I = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[5])
I1 = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[1])
I2 = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[2])
U1 = -np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[3])
U2 = -np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[4])
# U = np.genfromtxt("measurements_hall.txt", skip_header=1, usecols=[6])  # Broken ker je treba na roke dodat minus ker ga nisi prepisal
U = 0.5*(U2-U1)
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
plt.text(0.53, 0.12, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#a9f5ee", alpha=0.5))
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
e_0 = 1.6 * 10**-19
T_kelvin = T + 273
xdata = 1/((k*T_kelvin)/np.abs(e_0))
print(xdata)
ydata = -(I * B)/(U * c * e_0)
ed_xdata = xdata[7:]
print(ed_xdata)
ed_ydata = ydata[7:]
eg_xdata = xdata[:3]
print(ed_xdata)
eg_ydata = ydata[:3]
edfitpar, edfitcov = curve_fit(linear, xdata=ed_xdata, ydata=np.log(ed_ydata))
egfitpar, egfitcov = curve_fit(linear, xdata=eg_xdata, ydata=np.log(eg_ydata))
edfit = linear(xdata, edfitpar[0], edfitpar[1])
egfit = linear(xdata, egfitpar[0], egfitpar[1])
edfittext= "Linear fit 1: $y_1 = k_1x + n_1$\n$k_1$ = {} ± {}\n$n_1$ = {} ± {}".format(format(edfitpar[0], ".4e"), format(edfitcov[0][0]**0.5, ".4e"),
                                                                                   format(edfitpar[1], ".4e"), format(edfitcov[1][1]**0.5, ".4e"))
plt.text(0.525, 0.75, edfittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#FFB9BE", alpha=0.5))
egfittext= "Linear fit 2: $y_2 = k_2x + n_2$\n$k_2$ = {} ± {}\n$n_2$ = {} ± {}".format(format(egfitpar[0], ".4e"), format(egfitcov[0][0]**0.5, ".4e"),
                                                                                   format(egfitpar[1], ".4e"), format(egfitcov[1][1]**0.5, ".4e"))
plt.text(0.525, 0.55, egfittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor="#9EE4E6", alpha=0.5))
plt.plot(xdata, edfit, label=r"Linear fit 1", ls="--", alpha=0.8, color="#FF6D77")
plt.plot(xdata, egfit, label=r"Linear fit 2", ls="--", alpha=0.8, color="#0FACDB")
plt.title(r"$\ln{n}$ v odvisnosti od $\frac{1}{k_B T}$")
plt.xlabel(r"$(eV)^{-1}$")
plt.ylabel(r"$\ln{n}$")
plt.plot(xdata, np.log(ydata), color="#DC8FFF")
plt.ylim(47, 48.3)
plt.legend()
plt.show()

# Dual plot R_1(T)/R_2(T)
fig, (ax1, ax2) = plt.subplots(1, 2)
R1 = U1/I1
R2 = U2/I2
# plt.suptitle("Ohmska upornost v odvisnosti od temperature")
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
