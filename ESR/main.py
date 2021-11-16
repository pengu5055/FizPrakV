import matplotlib.pyplot as plt
import numpy as np

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
plt.plot(I2, U2, color="#7B64B0", alpha=0.4)
plt.plot(I3, U3, color="#92519C", alpha=0.4)
plt.errorbar(I1, U1, yerr=U1_err,  markersize=3, color="#7BD3D4", linestyle='None', marker="o", capsize=2, label=r"80 MHz", alpha=1)
plt.errorbar(I2, U2, yerr=U2_err,  markersize=3, color="#7763AF", linestyle='None', marker="o", capsize=2, label=r"85 MHz", alpha=1)
plt.errorbar(I3, U3, yerr=U3_err,  markersize=3, color="#8E509B", linestyle='None', marker="o", capsize=2, label=r"90 MHz", alpha=1)

plt.title(" ")
plt.xlabel("I [mA]")
plt.ylabel("U [mV]")
plt.legend()
plt.show()
