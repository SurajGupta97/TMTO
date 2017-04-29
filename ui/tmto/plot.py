import matplotlib as mpl
mpl.use('Agg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from iteration import *
import time,os
from datetime import datetime

def plot(cipher, N,plainText,iter):
	
	# os.remove('tmto/static/img/plot.png')
	fig = plt.figure(figsize=(10, 10))
	ax = fig.gca(projection='3d')

	# Make data.
	n = int(N)**(1/2.0)
	m = np.around(np.arange(0, n, (n/10.0)))
	t = np.around(np.arange(0, n, (n/10.0)))
	m, t = np.meshgrid(m, t)
	# R = np.sqrt(m**2 + t**2)
	w, h = 10, 10;
	Z = [[0 for x in range(w)] for y in range(h)] 

	for i in range(1,11):
		for j in range(1,11):
			Z[i-1][j-1] = function22(cipher, i, j, N, plainText, iter)
			# print Z
	Z = np.array(Z)
	print Z.shape,m.shape
	print m
	Z = Z.reshape(m.shape)

	# Plot the surface.
	surf = ax.plot_surface(m, t, Z, cmap=cm.coolwarm,
	                       linewidth=0, antialiased=False)

	# Customize the z axis.
	ax.set_zlim(0, 1)
	# ax.zaxis.set_major_locator(LinearLocator(10))
	# ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
	ax.set_xlabel('\n'+ 'm',fontsize=18)
	ax.set_ylabel('\n'+'t',fontsize=18)
	ax.set_zlabel('P(S)',fontsize=18,linespacing=60)
	ax.dist = 8

	# Add a color bar which maps values to colors.
	fig.colorbar(surf, orientation='horizontal')

	timestamp = str(datetime.now())
	path = 'tmto/static/img/plot' + timestamp + '.png'
	plt.savefig(path,dpi=200)
	time.sleep(5)
	return 'plot'+timestamp+'.png'
