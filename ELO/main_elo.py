import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr
from scipy.optimize import curve_fit


def linear(x, k, n):
    return k*x + n


c1, c2, c3 = cmr.take_cmap_colors("cmr.bubblegum", 3, cmap_range=(0.3, 1), return_fmt="hex")
d1, d2, d3 = cmr.take_cmap_colors("cmr.cosmic", 3, cmap_range=(0.35, 1), return_fmt="hex")

data1 = np.column_stack(np.genfromtxt("data1.csv", delimiter=",", skip_header=1))
u1 = data1[0]
u1_err = [0.01*i for i in u1]
x1 = data1[1]
x1_err = [0.01*i for i in x1]
y1 = data1[2]
y1_err = [0.01*i for i in y1]

fitpar1, fitcov1 = curve_fit(linear, u1, x1)
fitpar2, fitcov2 = curve_fit(linear, u1, y1)

fit1 = linear(u1, fitpar1[0], fitpar1[1])
fit2 = linear(u1, fitpar2[0], fitpar2[1])

# Plot
fig, ax = plt.subplots()
fittext1= "Linear fit: $y = kx + n$\n$k$ =  {} ± {}\n$n$ = {} ± {}"\
    .format(format(fitpar1[0], ".4e"), format(fitcov1[0][0]**0.5, ".4e"),
            format(fitpar1[1], ".4e"), format(fitcov1[1][1]**0.5, ".4e"))
plt.text(0.54, 0.55, fittext1, ha="left", va="center", size=10, transform=ax.transAxes,
         bbox=dict(facecolor=c3, alpha=0.5))

fittext2= "Linear fit: $y = kx + n$\n$k$ = {} ± {}\n$n$ = {} ± {}"\
    .format(format(fitpar2[0], ".4e"), format(fitcov2[0][0]**0.5, ".4e"),
            format(fitpar2[1], ".4e"), format(fitcov2[1][1]**0.5, ".4e"))
plt.text(0.54, 0.35, fittext2, ha="left", va="center", size=10, transform=ax.transAxes,
         bbox=dict(facecolor=c2, alpha=0.5))

plt.errorbar(u1, x1, yerr=x1_err,  markersize=2, color=d1,
             linestyle='None', marker="o", capsize=2, alpha=1, label=r"$\psi_r$")
plt.errorbar(u1, y1, yerr=y1_err,  markersize=2, color=d2,
             linestyle='None', marker="o", capsize=2, alpha=1, label=r"$\psi_i$")
plt.plot(u1, fit1, c=c3)
plt.plot(u1, fit2, c=c2)
plt.legend()

plt.title("Sorazmernost odziva z modulacijo")
plt.xlabel(r"$U_s$ [V]")
plt.ylabel(r"$\psi$ [V]")
plt.show()


# ----- Second Part -----
def model1(omega, psi0, tau):
    return psi0/(1 + (omega*tau)**2)


def model2(omega, psi0, tau):
    return -(psi0*omega*tau)/(1 + (omega*tau)**2)


data2 = np.column_stack(np.genfromtxt("data2.csv", delimiter=",", skip_header=1))

f2 = data2[0] * (2 * np.pi)
x2 = data2[1]
x2_err = [0.01*i for i in x2]
y2 = data2[2]
y2_err = [0.01*i for i in y2]

lag1 = 10
lag1b = len(x2)
lag2 = 20
lag2b = len(y2)
fitpar1, fitcov1 = curve_fit(model1, f2[lag1:lag1b], x2[lag1:lag1b], p0=[0.75, 0.02], bounds=([0.5, 0.001], [1, 1]))
fitpar2, fitcov2 = curve_fit(model2, f2[lag2:lag2b], y2[lag2:lag2b], p0=[1, 1], bounds=([0, 0], [2, 2]))

fit1 = model1(f2[lag1:lag1b], fitpar1[0], fitpar1[1])
fit2 = model2(f2[lag2:lag2b], fitpar2[0], fitpar2[1])

fig, ax = plt.subplots()
fittext1 = "Model fit: $\psi_r$\n$\psi_0$ =  {} ± {}\n$\\tau$ = {} ± {}"\
    .format(format(fitpar1[0], ".4e"), format(fitcov1[0][0]**0.5, ".4e"),
            format(fitpar1[1], ".4e"), format(fitcov1[1][1]**0.5, ".4e"))
plt.text(0.54, 0.75, fittext1, ha="left", va="center", size=10, transform=ax.transAxes,
         bbox=dict(facecolor=c3, alpha=0.5))

fittext2 = "Model fit: $\psi_i$\n$\psi_0$ = {} ± {}\n$\\tau$ = {} ± {}"\
    .format(format(fitpar2[0], ".4e"), format(fitcov2[0][0]**0.5, ".4e"),
            format(fitpar2[1], ".4e"), format(fitcov2[1][1]**0.5, ".4e"))
plt.text(0.54, 0.55, fittext2, ha="left", va="center", size=10, transform=ax.transAxes,
         bbox=dict(facecolor=c2, alpha=0.5))


plt.errorbar(f2, x2, yerr=x2_err,  markersize=2, color=d2,
             linestyle='None', marker="o", capsize=2, alpha=1, label=r"$\psi_r$")
plt.errorbar(f2, y2, yerr=y2_err,  markersize=2, color=d3,
             linestyle='None', marker="o", capsize=2, alpha=1, label=r"$\psi_i$")
plt.plot(f2[lag1:lag1b], fit1, c=c3)
plt.plot(f2[lag2:lag2b], fit2, c=c2)

plt.title("Komponenti signala kot funkciji frekvence")
plt.xlabel(r"$\omega$ [$s^{-1}$]")
plt.ylabel(r"$\psi$ [V]")
plt.legend()
plt.show()

print(fitpar1[1], fitcov1[1][1]**0.5)
print(fitpar2[1], fitcov2[1][1]**0.5)


# Third plot
def model_1_2(omega, tau, delay):
    psi0 = 1
    return model1(omega-delay, psi0, tau)/model2(omega-delay, psi0, tau)


lag = 25
lagb = len(x2 / y2) - 30

fitpar, fitcov = curve_fit(linear, f2[lag:lagb], (y2 / x2)[lag:lagb], p0=[fitpar1[1], 52])
fit = linear(f2[lag:lagb], *fitpar)

fittext1 = "Linear fit: $y = kn + n$\n$k$ = {} ± {}\n$n$ = {} ± {}".format(format(fitpar[0], ".4e"), format(fitcov[0][0]**0.5, ".4e"),
                                                                           format(fitpar[1], ".4e"), format(fitcov[1][1]**0.5, ".4e"))
plt.text(0.5, 0.75, fittext1, ha="left", va="center", size=10, transform=ax.transAxes,
         bbox=dict(facecolor=c2, alpha=0.5))

plt.errorbar(f2[lag:lagb], (y2 / x2)[lag:lagb], yerr=np.array(x2_err[lag:lagb]), markersize=2, color=d2,
             linestyle='None', marker="o", capsize=2, alpha=1, label=r"$\psi_r/\psi_i$")
plt.plot(f2[lag:lagb], fit, c=c2)

plt.title("Razmerje med signaloma")
plt.xlabel(r"$\omega$ [$s^{-1}$]")
plt.ylabel(r"$\psi_i/\psi_r$")
plt.show()
print(fitpar[0], fitcov[0][0]**0.5)
