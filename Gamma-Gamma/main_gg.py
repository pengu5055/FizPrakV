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

# Coincidence peaks
data_corr = np.column_stack(np.genfromtxt("korelacija_zoom1.txt", skip_header=12))
t_corr = data_corr[0] / 1.0e+09
c_corr = data_corr[1]
pde_corr = data_corr[2]

plt.bar(t_corr, pde_corr, color=c1, width=(t_corr[1] - t_corr[0]))

plt.title(r"Koincidenčni vrh")
plt.xlabel("t [ms]")
plt.ylabel("R [1/ps]")
plt.show()

data_corr = np.column_stack(np.genfromtxt("korelacija_rand1.txt", skip_header=12))
t_corr = data_corr[0] / 1.0e+09
c_corr = data_corr[1]
pde_corr = data_corr[2]

plt.bar(t_corr, pde_corr, color=c1, width=(t_corr[1] - t_corr[0]))

plt.title("Naključni koincidenčni \"vrh\"")
plt.xlabel("t [ms]")
plt.ylabel("R [1/ps]")
plt.show()

# Angle correlation of coincidence peaks
t_0_1, c_0_1, p_0_1 = np.column_stack(np.genfromtxt("kot0_1.txt", skip_header=12))
t_0_2, c_0_2, p_0_2 = np.column_stack(np.genfromtxt("kot0_2.txt", skip_header=12))
t_0_3, c_0_3, p_0_3 = np.column_stack(np.genfromtxt("kot0_3.txt", skip_header=12))
t_0 = (t_0_1 + t_0_2 + t_0_3)/3
c_0 = (c_0_1 + c_0_2 + c_0_3)/3
p_0 = (p_0_1 + p_0_2 + p_0_3)/3
t_5_1, c_5_1, p_5_1 = np.column_stack(np.genfromtxt("kot5_1.txt", skip_header=12))
t_5_2, c_5_2, p_5_2 = np.column_stack(np.genfromtxt("kot5_2.txt", skip_header=12))
t_5_3, c_5_3, p_5_3 = np.column_stack(np.genfromtxt("kot5_3.txt", skip_header=12))
t_5 = (t_5_1 + t_5_2 + t_5_3)/3
c_5 = (c_5_1 + c_5_2 + c_5_3)/3
p_5 = (p_5_1 + p_5_2 + p_5_3)/3
t_10_1, c_10_1, p_10_1 = np.column_stack(np.genfromtxt("kot10_1.txt", skip_header=12))
t_10_2, c_10_2, p_10_2 = np.column_stack(np.genfromtxt("kot10_2.txt", skip_header=12))
t_10_3, c_10_3, p_10_3 = np.column_stack(np.genfromtxt("kot10_3.txt", skip_header=12))
t_10 = (t_10_1 + t_10_2 + t_10_3)/3
c_10 = (c_10_1 + c_10_2 + c_10_3)/3
p_10 = (p_10_1 + p_10_2 + p_10_3)/3
t_15_1, c_15_1, p_15_1 = np.column_stack(np.genfromtxt("kot15_1.txt", skip_header=12))
# t_15_2, c_15_2, p_15_2 = np.column_stack(np.genfromtxt("kot15_2.txt", skip_header=12))
t_15_3, c_15_3, p_15_3 = np.column_stack(np.genfromtxt("kot15_3.txt", skip_header=12))
t_15 = (t_15_1 + t_15_3)/2
c_15 = (c_15_1 + c_15_3)/2
p_15 = (p_15_1 + p_15_3)/2
t_20_1, c_20_1, p_20_1 = np.column_stack(np.genfromtxt("kot20_1.txt", skip_header=12))
t_20_2, c_20_2, p_20_2 = np.column_stack(np.genfromtxt("kot20_2.txt", skip_header=12))
t_20_3, c_20_3, p_20_3 = np.column_stack(np.genfromtxt("kot20_3.txt", skip_header=12))
t_20 = (t_20_1 + t_20_2 + t_20_3)/3
c_20 = (c_20_1 + c_20_2 + c_20_3)/3
p_20 = (p_20_1 + p_20_2 + p_20_3)/3
t_25_1, c_25_1, p_25_1 = np.column_stack(np.genfromtxt("kot25_1.txt", skip_header=12))
t_25_2, c_25_2, p_25_2 = np.column_stack(np.genfromtxt("kot25_2.txt", skip_header=12))
t_25_3, c_25_3, p_25_3 = np.column_stack(np.genfromtxt("kot25_3.txt", skip_header=12))
t_25 = (t_25_1 + t_25_2 + t_25_3)/3
c_25 = (c_25_1 + c_25_2 + c_25_3)/3
p_25 = (p_25_1 + p_25_2 + p_25_3)/3
t_30_1, c_30_1, p_30_1 = np.column_stack(np.genfromtxt("kot30_1.txt", skip_header=12))
t_30_2, c_30_2, p_30_2 = np.column_stack(np.genfromtxt("kot30_2.txt", skip_header=12))
t_30_3, c_30_3, p_30_3 = np.column_stack(np.genfromtxt("kot30_3.txt", skip_header=12))
t_30 = (t_30_1 + t_30_2 + t_30_3)/3
c_30 = (c_30_1 + c_30_2 + c_30_3)/3
p_30 = (p_30_1 + p_30_2 + p_30_3)/3
t_40_1, c_40_1, p_40_1 = np.column_stack(np.genfromtxt("kot40_1.txt", skip_header=12))
t_40_2, c_40_2, p_40_2 = np.column_stack(np.genfromtxt("kot40_2.txt", skip_header=12))
t_40_3, c_40_3, p_40_3 = np.column_stack(np.genfromtxt("kot40_3.txt", skip_header=12))
t_40 = (t_40_1 + t_40_2 + t_40_3)/3
c_40 = (c_40_1 + c_40_2 + c_40_3)/3
p_40 = (p_40_1 + p_40_2 + p_40_3)/3
t_45_1, c_45_1, p_45_1 = np.column_stack(np.genfromtxt("kot45_1.txt", skip_header=12))
t_45_2, c_45_2, p_45_2 = np.column_stack(np.genfromtxt("kot45_2.txt", skip_header=12))
t_45 = (t_45_1 + t_45_2)/2
c_45 = (c_45_1 + c_45_2)/2
p_45 = (p_45_1 + p_45_2)/2
t_50_1, c_50_1, p_50_1 = np.column_stack(np.genfromtxt("kot50_1.txt", skip_header=12))
t_50_2, c_50_2, p_50_2 = np.column_stack(np.genfromtxt("kot50_2.txt", skip_header=12))
t_50 = (t_50_1 + t_50_2)/2
c_50 = (c_50_1 + c_50_2)/2
p_50 = (p_50_1 + p_50_2)/2
t_60_1, c_60_1, p_60_1 = np.column_stack(np.genfromtxt("kot60_1.txt", skip_header=12))
t_60_2, c_60_2, p_60_2 = np.column_stack(np.genfromtxt("kot60_2.txt", skip_header=12))
t_60 = (t_60_1 + t_60_2)/2
c_60 = (c_60_1 + c_60_2)/2
p_60 = (p_60_1 + p_60_2)/2

