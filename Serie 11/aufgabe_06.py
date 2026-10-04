import numpy as np
import matplotlib.pyplot as plt

data = np.load("xy1d.npy")
points = data.reshape(-1, 2)

x = points[:, 0]
y = points[:, 1]

plt.figure()
plt.plot(x, y, marker='o')
plt.axis('equal')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot der xy-Daten aus xy1d.npy")
plt.grid(True)
plt.show()
