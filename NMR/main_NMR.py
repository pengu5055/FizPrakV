import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr
from scipy.optimize import curve_fit


def exp(x, A, tau):
    return A*np.exp(-x/tau)


def exp2(x, A, tau):
    return A * (1 - np.exp(-x/tau))


c1, c2, c3 = cmr.take_cmap_colors("cmr.gem", 3, cmap_range=(0.3, 1), return_fmt="hex")

# Ion water T2 plot
data1_T2 = np.column_stack(np.genfromtxt("data2_T2.csv", delimiter=",", skip_header=1))
t1 = data1_T2[0]
u1 = data1_T2[1]
u1_err = [0.03 * i for i in u1]

fitpar, fitcov = curve_fit(exp, t1, u1, p0=[4, 3])
fit = exp(t1, *fitpar)

fig, ax = plt.subplots()
fittext = "Exp. fit: $y = U_0exp(-t/T_2)$\n$U_0$ = {} ± {}\n$T_2$ = {} ± {}"\
    .format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
            format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.5, 0.55, fittext, ha="left", va="center", size=10, transform=ax.transAxes,
         bbox=dict(facecolor=c2, alpha=0.5))

plt.errorbar(t1, u1, yerr=u1_err,  markersize=2, color=c2,
             linestyle='None', marker="o", capsize=2, alpha=1, label="Meritve")
plt.plot(t1, fit, c=c3)

plt.title("Signal spinskega odmeva")
plt.xlabel(r"$\tau$ [ms]")
plt.ylabel("U [mV]")
plt.legend()
plt.show()

# Ion water T1 plot
data3_T1 = np.column_stack(np.genfromtxt("data_glT1_ion.csv", delimiter=",", skip_header=1))
t1 = data3_T1[0]
u1 = data3_T1[1]
u1_err = [0.03 * i for i in u1]

fitpar, fitcov = curve_fit(exp2, t1, u1, p0=[4.39, 2.29])
fit = exp2(np.linspace(0, 500, 2000), *fitpar)

fig, ax = plt.subplots()
fittext = "Exp. fit: $y = U_0(1 - exp(-t/T_1))$\n$U_0$ = {} ± {}\n$T_1$ = {} ± {}"\
    .format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
            format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.5, 0.55, fittext, ha="left", va="center", size=10, transform=ax.transAxes,
         bbox=dict(facecolor=c2, alpha=0.5))

plt.errorbar(t1, u1, yerr=u1_err,  markersize=2, color=c2,
             linestyle='None', marker="o", capsize=2, alpha=1, label="Meritve")
plt.plot(np.linspace(0, 500, 2000), fit, c=c3)

plt.title("Signal proste precesije ion water")
plt.xlabel(r"$\tau$ [ms]")
plt.ylabel("U [mV]")
plt.legend()
plt.show()

# Tap water T1 plot
data4_T1 = np.column_stack(np.genfromtxt("data_glT1_tap.csv", delimiter=",", skip_header=1))
t1 = data4_T1[0]
u1 = data4_T1[1]
u1_err = [0.03 * i for i in u1]

fitpar, fitcov = curve_fit(exp2, t1, u1, p0=[1, 1])
fit = exp2(np.linspace(0, 100, 2000), *fitpar)

fig, ax = plt.subplots()
fittext = "Exp. fit: $y = U_0(1 - exp(-t/T_1))$\n$U_0$ = {} ± {}\n$T_1$ = {} ± {}"\
    .format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
            format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.5, 0.35, fittext, ha="left", va="center", size=10, transform=ax.transAxes,
         bbox=dict(facecolor=c2, alpha=0.5))

plt.errorbar(t1, u1, yerr=u1_err,  markersize=2, color=c2,
             linestyle='None', marker="o", capsize=2, alpha=1, label="Meritve")
plt.plot(np.linspace(0, 100, 2000), fit, c=c3)

plt.title("Signal proste precesije tap water")
plt.xlabel(r"$\tau$ [s]")
plt.ylabel("U [mV]")
plt.legend()
plt.show()
