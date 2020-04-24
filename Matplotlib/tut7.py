import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,5,2]
working = [7,8,7,2,3]
playing = [8,6,5,3,4]

slices = [7,2,2,13]
activities = ["sleeping" , "eating" , "working" , "playing"]
cols = ['c','m','r','g']




plt.pie(slices ,
        labels = activities ,
        colors = cols,
        shadow = True ,
        explode = (0,0.2,0,0),
        autopct = '%1.1f%%')

#plt.xlabel("X")
#plt.ylabel("Y")
plt.title("Pie plot")
#plt.legend()
plt.show()
