
import numpy as np
import matplotlib.pyplot as plt


theta=np.arange(-np.pi,np.pi,0.01)
r=1-np.sin(theta)

#create 2 subplot 
fig=plt.figure()
polor_ax=plt.subplot(121)
cart_ax=plt.subplot(122,projection='polar')
#cart_ax.axhline(y=0,color="green",_LineStyle="--")


#plot on cartersin 
cart_ax.plot(theta,r,'ro')

#plot on polar
polor_ax.plot(theta,r,'ro')


plt.show()