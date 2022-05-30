import random
import Linsys_func 
import numpy as np
minMax = 9
#length = random.randint(5,9)
length = 3
VectA = Linsys_func.vector_gen(length,-1*minMax,minMax)
VectB = Linsys_func.vector_gen(length,-1*minMax/3,minMax/3)
print("Vect A:",VectA," Vect B:",VectB)
fact = Linsys_func.ans_split(input("Type coeffiect of vect B: "))
powVectB = np.multiply(VectB,fact)
orthoVect = np.subtract(VectA,powVectB)
productVect = np.multiply(VectB,orthoVect)
print(np.rint(np.sum(productVect)))
