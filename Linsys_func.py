


import random
import numpy as np

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def row_operate(item):
    for i in range(len(item)):
        placey = i
        while item[placey][i] == 0:
            placey += 1
        item1 = func_a(item , i,placey)
        #printSq(item1)
        item = item1
    print("Ok")
    return item1

def func_a(item,place,row):
    temp = []
    fac = [i[place] for i in item]
    pivot = fac[row]
    times = [float(i/pivot)for i in fac]
    prime = item[place]
    for i in range(len(item)):
        if i == place:
            temp.append(item[i])
            continue
        han = zip(item[place],item[i])
        row = [z - y * times[i] for y,z in han]
        temp.append(row)
    return temp

def func_b(item):
    temp = []
    for i in item:
        sort = [k for k in i if k != 0]
        factor = sort[0]#min(sort)
        row = [j/factor for j in i]
        temp.append(row)
    return temp
def printSq(item):
    for i in item:
        print(i)
def switchDir(item):
    state = []
    for i in range(len(item[0])):
        col = []
        for j in item:
            col.append(j[i])
        state.append(col)
def linsys_take(item):
    coefficient = []
    solution = []
    for i in item:
        coefficient.append(i[0:-1])
        solution.append(i[-1])
    return coefficient , solution
def linsys_join(left,right):
    solution = []
    item = zip(left,right)
    for i,j in item:
        x = []
        x.extend(i)
        if type(j) is list:
            x.extend(j)
        else:
            x.append(j)
        solution.append(x)
    return  solution

def matrix_gen(col_height,row_width,min,max):
    item  = []
    for i in range(col_height):
        x = [float(random.randint(min,max))for i in range(row_width)]
        item.append(x)
    return item

def linalg_gen(col_height,row_width,min,max,ans = []):
    item = []
    if len(ans)<row_width:
        ans = [0 for i in range(row_width)]
    for i in range(col_height):
        x = [float(random.randint(min,max))for i in range(row_width)]
        store = 0
        for j in range(len(x)):
            store += ans[j]*x[j]
        x.append(store)
        item.append(x)
    return item

def vector_gen(length,min,max):
    return [float(random.randint(min,max))for i in range(length)]

def given_matrix(item):
    m = len(item)
    n = len(item[0])
    print("This is a ",m,"x",n," matrix with Domain:",n,"and Codomain:",m," in a mapping T: R",n," -> R",m)

def randPick(item,req):
    gotten = list(item)
    if req > len(item):
        print("error")
        return 0 
    handback = []
    for i in range(req):
        j = random.randint(0,len(gotten)-1)
        xd = gotten[j]
        handback.append(xd)
        gotten.remove(xd)
    return handback
    

def ans_checker(ans):
    for i in ans:
        check = ans_split(input("Enter:"))
        if check == i:
            print("correct!")
        elif i == 0 and check <= 0.02 and check >= -0.02 :
            print("correct!")
        elif check <= i*1.02 and check >= i*0.98 and check > 0:
            print("correct!")
        elif check >= i*1.02 and check <= i*0.98 and check < 0:
            print("correct!")
        else:
            print("Wrong!", i)

# Handle fraction input
def ans_split(user_input):
    numTerm = user_input.split('/')
    add = 0
    if len(numTerm)==2:
        add = float(numTerm[0])/float(numTerm[1])
    elif len(numTerm)==3:
        x = abs(float(numTerm[0])) +float(numTerm[1])/float(numTerm[2])
        if float(numTerm[0])<0:
            add -= x
        else:
            add = x
    elif len(numTerm)==4:
        print("Number error!")
    else:
        add = float(numTerm[0])
    return add

def zigzag(x):
    z = []
    if type(x) is list:
        for i in x:
            if type(i) is list:
                for j in i:
                    z.append(j)
            else:
                z.append(i)
    else:
        z.append(x)
    return z

def colRemove(x,loc):
    y = []
    for i in x:
        stor = []
        for j in range(len(i)):
            if list(loc).count(j+1)==0:
                stor.append(i[j])
        y.append(stor)
    return y


# import numpy as np

def row_echelon(A):
    """ Return Row Echelon Form of matrix A """

    # if matrix A has no columns or rows,
    # it is already in REF, so we return itself
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i,0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        B = row_echelon(A[:,1:])
        # and then add the first zero-column back
        return np.hstack([A[:,:1], B])

    # if non-zero element happens not in the first row,
    # we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # we divide first row by first element in it
    A[0] = A[0] / A[0,0]
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column
    A[1:] -= A[0] * A[1:,0:1]

    # we perform REF on matrix from second row, from second column
    B = row_echelon(A[1:,1:])

    # we add first row and first (zero) column, and return
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])

# A = np.array([[4, 7, 3, 8],
#               [8, 3, 8, 7],
#               [2, 9, 5, 3]], dtype='float')

# row_echelon(A)

def truefalsefind(array,item = False):
    for i in array:
        if i == item:
            return True
    else:
        return False

def eigenmatFind(n,r):
    sto = []
    eigenvaluelist = []
    while True:
        minnum = r*-1
        sto = matrix_gen(n,n,minnum,r)
        eigenvaluelist,eigenvectlist = np.linalg.eig(sto)
        sft  = np.real(eigenvaluelist)
        con1 = np.isreal(eigenvaluelist)
        con2 = [is_integer(n)for n in sft]
        if truefalsefind(con1,False)==False and truefalsefind(con2,False)==False:
            return sto, eigenvaluelist,eigenvectlist
            
# type a vector
def vector_typo(n):
    vec = []
    for i in range(n):
        word = "Type element "+str(i)+" of vector."
        num = ans_split(input(word))
        vec.append(num)
    return vec
def eigenvectcheck(matrix,eigenvect):
    values = []
    othside = np.matmul(matrix,eigenvect)
    store = np.divide(othside,eigenvect, out=np.zeros((len(eigenvect),len(eigenvect[0])), dtype=float), where=eigenvect!=0)
    nv = zip(np.transpose(store),np.transpose(eigenvect))
    for i,j in nv:
        #mater = zip(i,j)
        #k = [l//m for l,m in mater if int(m) != 0]
        i2 = np.rint(i)
        if np.all(i2 == i2[0]):
            xv = []
            xv.append(i[0])
            xv.append(j)
            values.append(xv)
        
    return values

def linIndCheck(item1,item2):
    if len(item1)!=len(item2):
        return False
    store = np.divide(item1,item2, out=np.zeros(len(item2), dtype=float), where=item2!=0)
    if np.all(store == store[0]):
        return False
    else:
        return True
def arrayloopequal(bank,req):
    for i in bank:
        if np.array_equal(i,req):
            return True
    else:
        return False
def matrix_row_opr(matrix,cutter,dest):
    length = len(matrix[0])
    row = matrix[dest]
    for i in range(length):
        factor = np.multiply(matrix[i],cutter[i])
        stupid = list(np.subtract(row,factor))
        row = stupid
    matrix[dest]=row
    return matrix

# print(matrix_row_opr([[1,1],[1,1],[1,1]],[1,0],2))