import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr
from scipy.optimize import curve_fit


def linear(x, k, n):
    return k*x + n


c1, c2, c3 = cmr.take_cmap_colors("cmr.gem", 3, cmap_range=(0.2, 1), return_fmt="hex")
data = np.column_stack(np.genfromtxt("data.csv", delimiter=",", skip_header=1))

plt.errorbar(data[0], data[1], yerr=[0.02*i for i in data[1]],  markersize=2, color=c2,
             linestyle='None', marker="o", capsize=2, alpha=1, label=r"Meritve")
plt.plot(data[0], data[1], c=c3, alpha=0.2)
plt.title(r"Časovna odvisnost $Y_{\mathrm{max}}^2$")
plt.xlabel("t [min]")
plt.ylabel(r"$Y_{\mathrm{max}}^2$ [cm]")
plt.show()

x = data[0] * 60  # Transform to seconds
y = 1/((data[1]/100)**2)
y_err = [0.03 * i for i in y]

lag = 0
lagb = len(x) - 5

x = x[lag:lagb]
y = y[lag:lagb]
y_err = y_err[lag:lagb]

fitpar, fitcov = curve_fit(linear, x, y)
fit = linear(x, *fitpar)
fig, ax = plt.subplots()
plt.errorbar(x, y, yerr=y_err,  markersize=2, color=c2,
             linestyle='None', marker="o", capsize=2, alpha=1, label=r"Meritve")
plt.plot(x, fit, c=c3)
fittext2= "Linear fit: $y = kx + n$\n$k$ = {} ± {}\n$n$ = {} ± {}"\
    .format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
            format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.52, 0.35, fittext2, ha="left", va="center", size=10, transform=ax.transAxes,
         bbox=dict(facecolor=c3, alpha=0.5))


plt.title(r"Časovna odvisnost $1/Y_{\mathrm{max}}^2$ pred skokom")
plt.xlabel("t [s]")
plt.ylabel(r"$1/Y_{\mathrm{max}}^2$ [$\mathrm{m}^{-2}$]")
plt.legend()
plt.show()
