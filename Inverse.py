import random
import scipy
import numpy as np
import Linsys_func 
n = 3
item = []
sto = Linsys_func.matrix_gen(n,n,-9,9)
iden = np.identity(n).tolist()
ans = np.linalg.inv(sto)
shon = Linsys_func.linsys_join(sto,iden)

for i in shon:
    print(i)
ansflat = Linsys_func.zigzag(ans)
Linsys_func.ans_checker(ansflat)

# for i in range(n):
#     x = [random.randint(-5,5)for i in range(n)]
#     x2 = []
#     for j in range(n):
#         if j==i:
#             x2.append(1)
#         else:
#             x2.append(0)
#     item.append(x+x2)