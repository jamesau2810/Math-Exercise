
import random
import Linsys_func 
import numpy as np

n = 3
ans = [float(random.randint(-9,9))for i in range(n)]
item = []
item = Linsys_func.linalg_gen(n,n,-9,9,ans)
"""for i in range(n):
    x = [float(random.randint(-9,9))for i in range(n)]
    store = 0
    for j in range(len(x)):
        store += ans[j]*x[j]
    x.append(store)
    item.append(x)"""
for i in item:
    print(i)
x,y = Linsys_func.linsys_take(item)

v = np.linalg.solve(x,y)
print(v)

#item4 = Linsys_func.row_operate(item)
#item3 = Linsys_func.row_operate(item)
#item1 = Linsys_func.func_b(item3)
#item = item1
#for i in item:
#    print(i)


"""item1 = func_a(item , 0)
for i in item1:
    print(i)
item2 = func_a(item1 ,1)
for i in item2:
    print(i)
item3 = func_a(item2 ,2)
for i in item3:
    print(i)"""
        
