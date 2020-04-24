from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(111,projection = '3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,9,5,4,3,2,1,0]
z = [1,2,5,4,9,8,7,5,3,2]

ax1.plot_wireframe(x,y,z)

ax1.set_xlabel('x-axis')

ax1.set_ylabel('y-axis')

ax1.set_zlabel('z-axis')

plt.show()
