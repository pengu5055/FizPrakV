import numpy as np
import matplotlib.pyplot as plt
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
time_bins = data_decay[0] / 1.0e+09  # Convert from ps to ms
pdf = data_decay[2]
plt.bar(time_bins, pdf, color=c1, width=0.2)

plt.title(r"Radioaktivni razpad $^{22}\mathrm{Na}$")
plt.xlabel("t [ms]")
plt.ylabel("R [1/ps]")
plt.show()
