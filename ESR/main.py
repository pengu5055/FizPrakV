import matplotlib.pyplot as plt
import numpy as np


def b_field(I):
    N = 1557
    mu = 4*np.pi * 10**-7
    d = 0.183
    return (N*mu*I)/d


def landau_g(x):
    bm = 9.27 * 10**-24
    h = 6.62 * 10 ** -34
    return h/(bm * x)


I1 = np.genfromtxt("ESR_80MHz.txt", skip_header=1, usecols=0)
U1 = np.genfromtxt("ESR_80MHz.txt", skip_header=1, usecols=1)
I2 = np.genfromtxt("ESR_85MHz.txt", skip_header=1, usecols=0)
U2 = np.genfromtxt("ESR_85MHz.txt", skip_header=1, usecols=1)
I3 = np.genfromtxt("ESR_90MHz.txt", skip_header=1, usecols=0)
U3 = np.genfromtxt("ESR_90MHz.txt", skip_header=1, usecols=1)
U1_err = [0.05 * element for element in U1]
U2_err = [0.05 * element for element in U2]
U3_err = [0.05 * element for element in U3]

plt.plot(I1, U1, color="#7BCFD4", alpha=0.4)
plt.errorbar(I1, U1, yerr=U1_err,  markersize=3, color="#7BD3D4", linestyle='None', marker="o", capsize=2, label=r"80 MHz", alpha=1)
plt.axhline(alpha=1, ls=":", c="#adadad")
plt.title("Odvod absorpcijske črte pri 80 MHz")
plt.xlabel("I [mA]")
plt.ylabel("U [mV]")
plt.legend()
plt.show()

plt.plot(I2, U2, color="#7B64B0", alpha=0.4)
plt.errorbar(I2, U2, yerr=U2_err,  markersize=3, color="#7763AF", linestyle='None', marker="o", capsize=2, label=r"85 MHz", alpha=1)
plt.axhline(alpha=1, ls=":", c="#adadad")
plt.title("Odvod absorpcijske črte pri 85 MHz")
plt.xlabel("I [mA]")
plt.ylabel("U [mV]")
plt.legend()
plt.show()

plt.plot(I3, U3, color="#92519C", alpha=0.4)
plt.errorbar(I3, U3, yerr=U3_err,  markersize=3, color="#8E509B", linestyle='None', marker="o", capsize=2, label=r"90 MHz", alpha=1)
plt.axhline(alpha=1, ls=":", c="#adadad")
plt.title("Odvod absorpcijske črte pri 90 MHz")
plt.xlabel("I [mA]")
plt.ylabel("U [mV]")
plt.legend()
plt.show()

b1 = b_field(0.299)
b2 = b_field(0.312)
x = (b1 + b2)/2 / (90 * 10**6)
print(x)
print(b1, b2, np.abs(b1-b2), (b1 + b2)/2)
print(landau_g(x))
