import random
n = 3

ans = [random.randint(-9,9)for i in range(n)]
item = []
ending = []
for i in range(n):
    x = [random.randint(-9,9)for v in range(n)]
    
    store = 0
    for j in range(len(x)):
        store += ans[j]*x[j]
    ending.append(store)
    x.append(chr(97 + i))
    item.append(x)
for i in item:
    print(i)
print(ending)
print(ans)
"""
for i in ans:
    check = input("Enter:")
    if float(check) <= i*1.02 and float(check) >= i*0.98 and float(check) > 0:
        print("correct!")
    elif float(check) >= i*1.02 and float(check) <= i*0.98 and float(check) < 0:
        print("correct!")
    else:
        print("Wrong!", i)
       """ 