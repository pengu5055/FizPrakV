import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr

data_25 = np.column_stack(np.genfromtxt("ion_25.txt", skip_header=1))
data_30 = np.column_stack(np.genfromtxt("ion_30.txt", skip_header=1))
data_35 = np.column_stack(np.genfromtxt("ion_35.txt", skip_header=1))

R = 1.E+9  # Ohm

U_25 = data_25[0]
I_25 = data_25[1]/R
I_25_err = [0.01*element for element in I_25]
U_30 = data_30[0]
I_30 = data_30[1]/R
I_30_err = [0.01*element for element in I_30]
U_35 = data_35[0]
I_35 = data_35[1]/R
I_35_err = [0.01*element for element in I_35]

c1, c2, c3 = cmr.take_cmap_colors("cmr.cosmic", 3, cmap_range=(0.3, 1), return_fmt="hex")

plt.plot(U_25, I_25, alpha=0.3, c=c1)
plt.errorbar(U_25, I_25, yerr=I_25_err,  markersize=2, color=c1,
             linestyle='None', marker="o", capsize=2, label=r"25 kV", alpha=1)
plt.axhline(y=1.18e-9, color="#adadad", ls="--", alpha=0.5)
plt.plot(U_30, I_30, alpha=0.3, c=c2)
plt.errorbar(U_30, I_30, yerr=I_30_err,  markersize=2, color=c2,
             linestyle='None', marker="o", capsize=2, label=r"30 kV", alpha=1)
plt.axhline(y=2.175e-9, color="#adadad", ls="--", alpha=0.5)
plt.plot(U_35, I_35, alpha=0.3, c=c3)
plt.errorbar(U_35, I_35, yerr=I_35_err,  markersize=2, color=c3,
             linestyle='None', marker="o", capsize=2, label=r"25 kV", alpha=1)
plt.axhline(y=3.36e-9, color="#adadad", ls="--", alpha=0.5)

plt.title("Merjenje toka nasičenja v ionizacijski celici")
plt.xlabel(r"$U_s$ [V]")
plt.ylabel(r"$I_e$ [A]")

plt.legend()
plt.show()

U = np.array([25, 30, 35])
I = np.array([1.18e-9, 2.175e-9, 3.36e-9])
rho = 1.17  # kgm^-3
V = 0.00063  # m^3
dX = I/(V*rho)
dX_err = [0.01*element for element in dX]
plt.plot(U, dX, c=c2, alpha=0.3)
plt.errorbar(U, dX, yerr=dX_err,  markersize=2, color=c1,
             linestyle='None', marker="o", capsize=2, alpha=1)

plt.title("Hitrost ekspozicijske doze")
plt.xlabel("U [kV]")
plt.ylabel(r"$\frac{dX}{dt}$ [$A/kg$]")
plt.show()