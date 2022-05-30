import matplotlib.pyplot as plt
import numpy as np
import Linsys_func
g = Linsys_func.matrix_gen(2,2,-1,1)#[[1,0],[0,-1]]
h = Linsys_func.vector_gen(2,-9,9)
x =  list(np.matmul(g,h))
basket = [["transform matrix: ",g],
["input vector: ",h],["result vector: ",x]]
rearrange = Linsys_func.randPick(basket,3)

for i in rearrange[0:-1]:
    print(i[0])
    Linsys_func.printSq(i[1])
zi = Linsys_func.zigzag(rearrange[-1][1])
print("Find ",rearrange[-1][0])
Linsys_func.ans_checker(zi)
ax = plt.axes()
ax.arrow(0.0, 0.0, h[0], h[1])#, head_width=0.5, head_length=0.7, fc='lightblue', ec='black')
ax.arrow(0.0, 0.0, x[0], x[1])#, head_width=0.5, head_length=0.7, fc='lightblue', ec='black')
plt.grid()

plt.xlim(-10,10)
plt.ylim(-10,10)

plt.title('Output transform',fontsize=10)

#plt.savefig('how_to_plot_a_vector_in_matplotlib_fig1.png', bbox_inches='tight')
plt.show()
#plt.close()