import pandas as pd

data = pd.read_csv('products.csv')
data1=[5,15,25,35,45]
x=[1,2,3,4,5]
data2=[10,20,30,40,50]

import matplotlib.pyplot as plt
#plt.plot(data['ProductName'],data['Price'])
plt.subplot(3,3,1)
plt.scatter(x,data1,color='blue',label = '1st')
plt.scatter(x,data2,color='Red',label = '2nd')
plt.legend()


import matplotlib.pyplot as plt
import numpy as np
plt.subplot(3,3,2)
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints,color='green',marker = '+',linestyle=(0,(3,10,1,10,)),)

plt.subplot(3,3,3)
h=[10,20,30,40,50]
plt.bar(x=['A','B','C','D','E'],height=h,color='purple')


plt.subplot(3,3,4)

mylabels = ["Apples", "Bananas", "Cherries", "Dates","grapes"]

plt.pie(data1, labels = mylabels,autopct='%1.1f%%')

plt.show()

#18,19,