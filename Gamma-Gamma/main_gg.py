import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import cmasher as cmr

c1, c2, c3 = cmr.take_cmap_colors("cmr.cosmic", 3, cmap_range=(0.2, 1), return_fmt="hex")


# Time resolution of TDC
data_TDC = np.column_stack(np.genfromtxt("loc_24-4.txt", skip_header=12))
time_bins_tdc = data_TDC[0] / 1.0e+09
counts_tdc = data_TDC[1]
plt.bar(time_bins_tdc, counts_tdc, color=c1, width=(time_bins_tdc[1]-time_bins_tdc[0]))
print(np.std(data_TDC[1]))

plt.title(r"Časovna ločljivost TDC")
plt.xlabel("t [ms]")
plt.ylabel("N")
plt.show()


# Radioactive decay
data_decay = np.column_stack(np.genfromtxt("decay_0.txt", skip_header=12))
t_mes = 103.6
time_bins = data_decay[0] / 1.0e+09  # Convert from ps to ms
pdf = data_decay[2]
counts = data_decay[1]
plt.bar(time_bins, pdf, color=c1, width=0.2)

plt.title(r"Radioaktivni razpad $^{22}\mathrm{Na}$")
plt.xlabel("t [ms]")
plt.ylabel("R [1/ps]")
plt.show()

# Radioactive decay linear plot
def masking(x, y):
    mask = x > 0
    return x[mask], y[mask]


newc, newt = masking(counts, time_bins)

newc /= 30
dnewc = np.mean(newc) + np.zeros(len(newc))
dlog = dnewc / newc


def fit(x, k, n):
    return k * x + n


fig, ax = plt.subplots()
fitpar, fitcov = curve_fit(fit, xdata=newt, ydata=np.log(newc), sigma=dlog, absolute_sigma=True)
yfit = fit(newt, fitpar[0], fitpar[1])
fittext= "Linear fit 1: $y_1 = k_1x + n_1$\n$k_1$ = {} ± {}\n$n_1$ = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                                     format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.scatter(newt, np.log(newc), color=c2, s=3)
plt.plot(newt, yfit, color=c1)
plt.text(0.5, 0.9, fittext, ha="left", va="center", size=10, transform=ax.transAxes, bbox=dict(facecolor=c3, alpha=0.5))

plt.title(r"Lineariziran graf radioaktivnega razpada $^{22}\mathrm{Na}$")
plt.xlabel("t [ms]")
plt.ylabel(r"$\ln \left( \frac{\Delta p}{\Delta t}\right)$")
plt.show()
print(np.mean(counts)/t_mes)

