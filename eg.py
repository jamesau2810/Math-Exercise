# import Linsys_func
# import numpy
# import sys
# sys.path.append("/Users/jamesau/opt/anaconda3/lib/python3.8/site-packages/")
# #from sympy import *
# import sympy
# #sympy.init_printing()
# x, y, z = sympy.symbols("x y z")
# expr = sympy.cos(x)+1
# print(expr.subs(x,y))
# import importlib.util
# spec = importlib.util.spec_from_file_location('sympy','/Users/jamesau/opt/anaconda3/lib/python3.8/site-packages/sympy')
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)
# foo.init_printing()
#/Users/jamesau/opt/anaconda3/lib/python3.8/site-packages/sympy
# item = [[-6.0, -9.0, 5.0, 0],
# [-5.0, 0.0, -9.0, 0],
# [-7.0, -5.0, 7.0, 0]]
# x,y = Linsys_func.linsys_take(item)
# print(numpy.linalg.solve(x,y))
"""
item4 = Linsys_func.row_operate(item)
item3 = Linsys_func.row_operate(item4)
item1 = Linsys_func.func_b(item3)
item = item1
for i in item:
    print(i)
"""
# print("y =",Linsys_func.matrix_gen(3,3,-9,9))