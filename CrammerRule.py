import random
import Linsys_func 
import numpy as np

n = 3
ans = [float(random.randint(-9,9))for i in range(n)]
item = []
colRef = ['x','y','z','d']
item = Linsys_func.linalg_gen(n,n,-9,9,ans)
a,b = Linsys_func.linsys_take(item)

ans = np.linalg.solve(a,b)
base = np.linalg.det(a)
for i in range(n):
    detAlg = []
    a,b = Linsys_func.linsys_take(item)
    xa = zip(a,b)
    for j,k in xa:
        storAlg = []
        storAlg=j
        storAlg[i]=k
        detAlg.append(storAlg)
    #Linsys_func.printSq(detAlg)
    ansin = Linsys_func.zigzag(detAlg)
    Linsys_func.printSq(item)
    print("fina array",colRef[i])
    ansin.append(np.linalg.det(detAlg))
    Linsys_func.ans_checker(ansin)
#Linsys_func.printSq(a)
    