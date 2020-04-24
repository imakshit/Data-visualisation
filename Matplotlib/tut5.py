import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,3,5,7,4,3,2,6]

plt.scatter(x,y, label = 'skitscat' , color = 'k' , s = 100 , marker = '*')


plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter plot")
plt.legend()
plt.show()
