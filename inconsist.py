import random
import numpy as np
import Linsys_func
#import fractions
n = 3
ans = [random.randint(-9,9)for i in range(n)]
item = Linsys_func.linalg_gen(n,n,-9,9,ans)
ite = [random.randint(0,n-1)for i in range(2)]
Linsys_func.printSq(item)
print("Matrix inconsist if K in ",ite[0]+1," ",ite[1]+1)
user_input = input("k = ")
add = Linsys_func.ans_split(user_input)
item[ite[0]][ite[1]] += add
a,b = Linsys_func.linsys_take(item)

try:
    np.linalg.solve(a,b)
except np.linalg.LinAlgError:
    f = open("unsolvable.txt", "w")
    for i in item:
        f.write(str(i)+"\n")
    f.write("\n")
    f.close()
    print("Success: ")
else:
    print("fail: ")