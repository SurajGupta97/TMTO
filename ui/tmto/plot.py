from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from iteration import *


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
m = np.arange(1, 11)
t = np.arange(1, 11)
m, t = np.meshgrid(m, t)
# R = np.sqrt(m**2 + t**2)
w, h = 10, 10;
Z = [[0 for x in range(w)] for y in range(h)] 

for i in range(1,11):
	for j in range(1,11):
		Z[i-1][j-1] = function22('AES',i,j,256,10,50)
		# print Z
Z = np.array(Z)
Z = Z.reshape(m.shape)
# print Z
# R = np.sqrt(m**2 + t**2)
# Z = np.sin(R)
# print Z
# Plot the surface.
surf = ax.plot_surface(m, t, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()