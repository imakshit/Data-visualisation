import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,5,2]
working = [7,8,7,2,3]
playing = [8,6,5,3,4]


plt.plot([],[],color = 'm' , linewidth = 5 , label = "sleeping")
plt.plot([],[],color = 'c' , linewidth = 5 , label = "eating")
plt.plot([],[],color = 'r' , linewidth = 5 , label = "working")
plt.plot([],[],color = 'k' , linewidth = 5 , label = "playing")


plt.stackplot(days,sleeping,eating,working,playing ,colors = ['m','c','r','k'])


plt.xlabel("X")
plt.ylabel("Y")
plt.title("Stack plot")
plt.legend()
plt.show()
