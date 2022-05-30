
import random

import Linsys_func 
import numpy as np
import itertools
height = 3 #random.randint(2,4)
width = 4#height+random.randint(0,2)
x = Linsys_func.matrix_gen(height,width,-9,9)
y = np.transpose(x)
Linsys_func.printSq(x)
numColS = int(input("Enter number of "))
space = []
for i in range(numColS):
    xr = Linsys_func.vector_typo(height)
    space.append(xr)
hv = 0
if numColS == height:
    hv = height-numColS
else:
    hv = 1
igt = [i for i in itertools.permutations(y,hv)]
result = []
if numColS != height:
    for combin in igt:
        carr = list(combin) + space
        result.append(np.absolute(np.linalg.det(carr)))
else:
    # print(np.linalg.det())
    for i in y:
        try:
            np.linalg.solve(np.transpose(space),i)
        except np.linalg.LinAlgError:
            result.append(1)
        except np.linalg.ValueError:
            result.append(1)
        else:
            result.append(0)




if np.sum(result)<=0:
    print("Success")
else:
    print("Fail")
ansStore = []
print("Type null space of vector")
for xv in range(width-numColS):
    valid = False
    xg = Linsys_func.vector_typo(width)
    cumul = np.matmul(x,xg)
    if np.sum(cumul)==0:
        print("Correct")
    else:
        print("Wrong")

#Linsys_func.printSq(y)
# print(np.linalg.qr(x))
