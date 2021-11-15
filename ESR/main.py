import matplotlib.pyplot as plt
import numpy as np

I1 = np.genfromtxt("ESR_80MHz.txt", skip_header=1, usecols=0)
U1 = np.genfromtxt("ESR_80MHz.txt", skip_header=1, usecols=1)

plt.plot(I1, U1)
plt.show()
