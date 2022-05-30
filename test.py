import scipy.linalg
import Linsys_func
import numpy as np
x = Linsys_func.matrix_gen(3,4,-9,9)
Linsys_func.printSq(x)
p, l, u = scipy.linalg.lu(x)
Linsys_func.printSq(p)
Linsys_func.printSq(l)
Linsys_func.printSq(u)
#y = Linsys_func.row_echelon(np.array(x))

#Linsys_func.printSq(y)