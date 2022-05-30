import random
import Linsys_func 
import numpy as np
lengthy = random.randint(3,7)
vector_example = Linsys_func.vector_gen(lengthy,-9,9)
print(vector_example)
dotans = [x*x for x in vector_example]
sftans = [np.sqrt(np.sum(dotans))]
print("Type length: ")
Linsys_func.ans_checker(sftans)
unitans = [x*sftans[0] for x in vector_example]
print("Type unitvector: ")
Linsys_func.ans_checker(unitans)