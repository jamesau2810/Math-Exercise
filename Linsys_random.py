import random
import Linsys_func
import numpy as np
n = 3
item = []
item = Linsys_func.matrix_gen(n,n+1,-9,9)

Linsys_func.printSq(item)

a , b = Linsys_func.linsys_take(item)
ans = []
 



try:
    np.linalg.solve(a,b)
except np.linalg.LinAlgError:
    f = open("unsolvable.txt", "w")
    for i in item:
        f.write(i,"\n")
    f.close()
    print("No need to do ")
else:  
    solvent = np.linalg.solve(a,b)
    Linsys_func.ans_checker(solvent)
    

    
#for i in item:
#    a = 0
#    for j in range(n):
#        a += i[j]*ans[j]
#    print(a)

