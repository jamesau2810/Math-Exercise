"""import sys
sys.path.append('/Users/jamesau/Documents/GitHub/School_Train')
import ExamPract"""
import random
import Linsys_func
n = 3
ans = [random.randint(-9,9)for i in range(n)]
item = Linsys_func.linalg_gen(n,n,-9,9,ans)

for i in item:
    print(i)
Linsys_func.ans_checker(ans)
"""for i in ans:
    check = input("Enter:")
    if float(check) <= i*1.02 and float(check) >= i*0.98 and float(check) > 0:
        print("correct!")
    elif float(check) >= i*1.02 and float(check) <= i*0.98 and float(check) < 0:
        print("correct!")
    else:
        print("Wrong!", i)"""
        
