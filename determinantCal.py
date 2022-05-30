# from ast import Store
import numpy as np
import random
import Linsys_func
n = 3
matnum = 3
roundnum = 7
item = []
matron = []
meth = [random.randint(0,3)for i in range(roundnum)]
matchoic = [random.randint(0,matnum-1)for i in range(roundnum)]
storebit = 1
def funcgrp(item,number):
    if   number == 0:
        s = np.transpose(item)
        return np.linalg.det(s),"^t"
    elif number == 1:
        s = np.linalg.inv(item)
        return np.linalg.det(s),"^-1"
    elif number == 2:
        s = np.multiply(item,2)
        return np.linalg.det(s),"*2"
    elif number == 3:
        s = []
        for i in range(len(item)):
            cr = len(item)-1-i
            s.append(item[cr])
        return np.linalg.det(s),"r<->"
    # elif number == 4:
    #     return np.linalg.det(s)
    # elif number == 5:
    #     return np.linalg.det(s)

for i in range(matnum):
    item.append(chr(97+i))
    matron.append(Linsys_func.matrix_gen(n,n,-9,9))
ji = zip(item,matron)
for i,j in ji:
    print(i,":",np.linalg.det(j))
zi = zip(meth,matchoic)
for i,j in zi:
    intern = matron[j]
    res, des = funcgrp(intern,i)
    storebit *= res
    print(item[j]+des)
x = input()
print(storebit)
#meth.append()
out = zip(item,matron)

    