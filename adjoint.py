import random
import scipy
import numpy as np
import Linsys_func 

n = 3
item = []
sto = Linsys_func.matrix_gen(n,n,-9,9)
iden = np.identity(n).tolist()
item1 = np.linalg.inv(sto)
item2 = np.linalg.det(sto)
Linsys_func.printSq(item1)
ans = np.multiply(item1,item2)#[i/item2 for i in item1]
print(ans)
shon = Linsys_func.linsys_join(sto,iden)

for i in shon:
    print(i)
ansflat = Linsys_func.zigzag(ans)
Linsys_func.ans_checker(ansflat)
#np.multiply()