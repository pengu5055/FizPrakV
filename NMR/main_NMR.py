import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr
from scipy.optimize import curve_fit


def exp(x, A, tau):
    return A*np.exp(-x/tau)


c1, c2, c3 = cmr.take_cmap_colors("cmr.gem", 3, cmap_range=(0.3, 1), return_fmt="hex")

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

data