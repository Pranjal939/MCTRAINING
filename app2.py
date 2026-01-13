import pandas as pd

data = pd.read_csv('products.csv')
data1=[5,15,25,35,45]
x=[1,2,3,4,5]
data2=[10,20,30,40,50]

import matplotlib.pyplot as plt
#plt.plot(data['ProductName'],data['Price'])
plt.subplot(1,2,1)
plt.scatter(x,data1,color='blue',label = '1st')
plt.scatter(x,data2,color='Red',label = '2nd')
plt.legend(['Prive vs Unit'])
plt.legend()


import matplotlib.pyplot as plt
import numpy as np
plt.subplot(1,2,2)
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints,color='green',marker = '+',linestyle=(0,(3,10,1,10,)),)
plt.show()