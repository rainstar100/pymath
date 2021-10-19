
import numpy as np
import matplotlib.pyplot as plt


theta=np.arange(-np.pi,np.pi,0.01)
#theta=np.linspace(-1000,1000,2000) NO consider the function's propterty
r=1+np.cos(theta)
r_x=r*np.sin(theta)
r_y=r*np.cos(theta)

ax1=plt.subplot(221)
ax1.plot(r_x,r_y,'ro')

ax2=plt.subplot(222,projection="polar")
ax2.plot(theta,r,'ro')

ax3=plt.subplot(223)
ax3=plt.plot(theta,r)

plt.show()