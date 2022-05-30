import Linsys_func
import numpy as np
import random

n = 2#random.randint(2,5)

itemA = Linsys_func.matrix_gen(n,n,-9,9)
itemB = Linsys_func.matrix_gen(n,n,-9,9)
itemC = np.matmul(itemA,itemB)
print("B matrix")
Linsys_func.printSq(itemB)
print("Result matrix")
Linsys_func.printSq(itemC)
flat=Linsys_func.zigzag(itemA)
Linsys_func.ans_checker(flat)
