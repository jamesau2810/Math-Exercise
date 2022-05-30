
import numpy as np
import random
import Linsys_func
n = random.randint(2,5)
extens = 1
#extens = random.randint(0,3)
x = Linsys_func.matrix_gen(n,n+extens,-9,9)
b = list(np.zeros(n))
bank = Linsys_func.linsys_join(x,b)

Linsys_func.printSq(bank)
pickRow = []
for i in range(extens):
    pickRow.append(int(input("pick the "+str(i)+ " column: ")))

a = Linsys_func.colRemove(x,pickRow)

try:
    np.linalg.solve(a,b)
except np.linalg.LinAlgError:
    print("fail: ")
else:
    print("Success: ")
    print(np.linalg.solve(a,b))
#print(colRemove([[1,2,3],[4,5,6]],3))


np.tr