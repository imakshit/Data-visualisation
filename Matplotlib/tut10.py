from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


fig = plt.figure()
ax1 = fig.add_subplot(111,projection = '3d')

x = [1,2,3,4,5,6,7,8,9,10]
y = [5,6,7,9,5,4,3,2,1,0]
z = [1,2,5,4,9,8,7,5,3,2]

a = [-1,-3,4,7,5,2,8,9,3,1]
b = [-4,-5,-6,7,5,3,1,4,-9,-10]
c = [1,2,5,0,9,8,6,4,3,6]

ax1.scatter(x,y,z , c = 'g' , marker = 'x')
ax1.scatter(a,b,c , c = 'r' , marker = '*')

ax1.set_xlabel('x-axis')

ax1.set_ylabel('y-axis')

ax1.set_zlabel('z-axis')

plt.show()
