import numpy as np
import matplotlib.pyplot as plt
import cmasher as cmr

c1, c2, c3 = cmr.take_cmap_colors("cmr.cosmic", 3, cmap_range=(0.2, 1), return_fmt="hex")


# Radioactive decay
data = np.column_stack(np.genfromtxt("decay_0.txt", skip_header=12))
time_bins = data[0] / 1.0e+09  # Convert from ps to ms
counts = data[1]
print(time_bins)
print(counts)
plt.bar(time_bins, counts, color=c1, width=0.2)

plt.title(r"Radioaktivni razpad $^{22}\mathrm{Na}$")
plt.xlabel("t [ms]")
plt.ylabel("R [1/s]")
plt.show()
