import numpy as np
mx= arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
mx=mx.reshape(3,4)
for i in mx.transpose():
    print(i)