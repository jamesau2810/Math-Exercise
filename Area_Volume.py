from cProfile import label
from cmath import e
import random
from this import d
from tkinter import E
from xml.etree.ElementInclude import XINCLUDE
import Linsys_func 
import numpy as np
import matplotlib.pyplot as plt
n = 3
#n = random.randint(2,3)


#ax.quiver()
#ax.plot3D()
item = []
item = Linsys_func.matrix_gen(n,n,0,9)
color = ['b','g','r','c','m','y','k','w']
if len(item)==3:
    #Linsys_func.printSq(item)
    lop = list(zip(item[0],item[1],item[2],color[0:3]))
    #print(lop) 
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for a,b,c,d in lop:
        strit = str(a)+" "+str(b)+" "+str(c)
        ax.plot3D([0,a],[0,b],[0,c],d,label = strit)
    ax.set_xlim([0, 9])
    ax.set_ylim([0, 9])
    ax.set_zlim([0, 9])
    leg = plt.legend(loc='upper center')
    plt.title("Find Volume of paralelpipe")
    plt.show()
    
    Linsys_func.ans_checker([np.linalg.det(item)])
elif len(item)==2:
    Linsys_func.printSq(item)
    fig = plt.figure()
    ax = plt.axes()
    ax.plot(item[0],item[1])
    plt.title("Find Area of dot product")
    plt.show()
    Linsys_func.ans_checker([np.linalg.det(item)])
















# def makeVector(item,length = 3):
#     if type(item) is list:
#         intra = list(item)
#         while(len(intra)<length):
#             intra.append(0)
#         return intra
#     else:
#         return False