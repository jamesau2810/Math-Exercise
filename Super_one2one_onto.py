import numpy as np
import random
import Linsys_func
width = random.randint(2,5)
height = random.randint(2,5)
veclen = min(width,height)
anslen = max(width,height)
Amat = Linsys_func.matrix_gen(height,width,-9,9)
Linsys_func.printSq(Amat)
prevtype = []
suc = []
tokening = 0
vectorL = Linsys_func.vector_gen(veclen,-9,9)
if width==height:
    safe = np.linalg.det(Amat)
    if safe != 0:
        print("Possible one-to-one or onto")

if width>height or tokening == 2:
    print(vectorL)
    print("Type a vect:")
    ans = Linsys_func.vector_typo(anslen)
    bvect = np.matmul(Amat,ans)
    suc.append(np.array_equal(bvect,vectorL))
    prevtype.append(ans)
    print("Type another vect:")
    ans = Linsys_func.vector_typo(anslen)
    prevtype.append(ans)
    bvect = np.matmul(Amat,ans)
    suc.append(np.array_equal(bvect,vectorL))
    if Linsys_func.linIndCheck(prevtype[0],prevtype[1]) and Linsys_func.truefalsefind(suc,True):
        print("Done")
    else:
        print("Fail")
elif width<height or tokening == 3:
    ans = np.matmul(Amat,vectorL)
    print(vectorL)
    Linsys_func.ans_checker(ans)
    prevtype.append(ans)
    hander = Linsys_func.linsys_join(Amat,ans)
    for i in range(height-width):
        print("Type row operation for row",height-i)
        cutter = Linsys_func.vector_typo(width)
        hander = Linsys_func.matrix_row_opr(hander,cutter,height-i-1)
    print(hander)
    # for i in range(3):
    #     item = Linsys_func.vector_typo(veclen)
    #     ans = np.matmul(Amat,item)
    #     print(ans)
    
        
    

