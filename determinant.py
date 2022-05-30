import numpy as np
import random
import Linsys_func
n = random.randint(2,5)
item = Linsys_func.matrix_gen(n,n,-9,9)

ans = np.linalg.det(item)
for i in item:
    print(i)
q = input()
print(ans)