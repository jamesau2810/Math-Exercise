import random
import Linsys_func 
import numpy as np






n = 3
ans = [float(random.randint(-9,9))for i in range(n)]
item = []
item = Linsys_func.linalg_gen(n,n,-9,9,[0,0,0])

for i in item:
    print(i)
mat,sol = Linsys_func.linsys_take(item)
item1 = np.linalg.solve(mat,sol)
"""item4 = Linsys_func.row_operate(item)
item3 = Linsys_func.row_operate(item4)
item1 = Linsys_func.func_b(item3)"""
item = item1

for i in item:
    print(i)


"""for i in range(n):
    x = [float(random.randint(-9,9))for i in range(n)]
    store = 0
    #for j in range(len(x)):
    #    store += ans[j]*x[j]
    #x.append(store)
    x.append(0)
    item.append(x)"""