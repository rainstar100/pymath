import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.linspace(0,1,100)
y=np.linspace(0,1,100)
z=np.eye(100)

for i in range(x.size):
    for j in range(y.size):
        z[i][j]=x[i]+y[j]

print(z.shape)

fig=plt.figure()
ax=Axes3D(fig)
x,y=np.meshgrid(x,y)


ax=fig.add_subplot(111,projection="3d")
ax.plot_surface(x,y,z,rstride=1, cstride=1, cmap='hot')



plt.show()


