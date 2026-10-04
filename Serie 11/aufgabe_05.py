import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2            # f(x,y)
T = -8*X + 8*Y             # Tangentialebene

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Funktion
ax.plot_surface(X, Y, Z, alpha=0.6)

# Tangentialebene
ax.plot_surface(X, Y, T, alpha=0.6)

# Tangentialpunkt
ax.scatter(-4, 4, 32, color='red', s=50)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("f(x,y) = x² + y² und Tangentialebene im Punkt (-4,4)")

plt.show()
