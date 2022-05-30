import random
n = random.randint(1,20)
bag = range(n)
print(n)
item = "v = [x for x in bag if x"+ input("Type inequalities: ")+ "]"
exec(item)
#print(v)