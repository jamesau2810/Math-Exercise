# import importlib
import numpy as np
import Linsys_func

# from pytest import fail 
n = 3
intre = 9
item = []
condi = []
sto = []
# heav = []

sto , eigenlist,eigenvect = Linsys_func.eigenmatFind(n,intre)
eigenlist = sorted(eigenlist)
# iden = np.identity(n).tolist()
Linsys_func.printSq(sto)
print("Type eigenvalues, smallest to largest: ")
Linsys_func.ans_checker(eigenlist)
values = Linsys_func.eigenvectcheck(sto,eigenvect)
for i in values:
    print("Find eigenvectors corresponding to",i[0])
    Linsys_func.ans_checker(i[1])

if len(eigenvect[0])>=n:
    inveigen = np.linalg.inv(eigenvect)
    pro1 = np.matmul(inveigen,sto)
    res = np.matmul(pro1,eigenvect)
    Linsys_func.printSq(np.rint(res))




#Linsys_func.printSq(eigenvect)
# Linsys_func.printSq(iden)
# num = int(input("Eigenvalue: "))
# iden1 = np.multiply(iden,num)
# item = np.subtract(sto,iden1)
# num1 = np.linalg.det(item)
# if num1>=-0.01 and num1<=0.01:
#     print("Success!")
# else:
#     print("fail")
# eignvect = []
# for i in range(n):
#     qty = "Eigenvector item "+str(i)+":"
#     x = int(input(qty))
#     eignvect.append(x)
# bvect = np.matmul(sto,eignvect)
# cxp = np.true_divide(bvect,eignvect)
# for i in cxp:
#     if i != cxp[0] and i!=0:
#         print("Fail")
#         break
# else:
#     print("Eigenvalue found",cxp[0],", Eigenvector found!",eignvect)
    

# p_x_female = scipy.stats.norm.sf(t,loc = m_x_gender['Female'],scale = sd_x_gender['Female'])
# p_x_male = scipy.stats.norm.cdf(t,loc = m_x_gender['Male'],scale = sd_x_gender['Male'])#cdf
# scipy.stats.norm.cdf(x,loc = m_by_species['Iris-virginica'],scale = sd_by_species['Iris-virginica'])+
# scipy.stats.norm.sf(t,loc = m_by_species['Iris-setosa'],scale = sd_by_species['Iris-setosa'])