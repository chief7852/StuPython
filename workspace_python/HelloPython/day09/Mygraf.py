import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np                
import matplotlib.pyplot as plt   
from day06 import MysqlConfig


mpl.rcParams['legend.fontsize'] = 10        

fig = plt.figure()                                
ax = fig.gca(projection='3d')
# x 축 = 종목 y축 = 시간 z축 = 가격
zs = []
x = np.zeros(10)
y = range(10)
zs.append([1,3,2,5,6,2,3,4,5,1])
zs.append([1,3,3,4,6,7,1,1,2,1])
zs.append([1,3,5,8,1,2,5,6,7,1])
z1 = [1,3,2,5,6,2,3,4,5,1]

                    
ax.plot(x, y, zs[0], label='samsung')      
ax.plot(x+1, y, zs[1], label='lg')      
ax.plot(x+2, y, zs[2], label='sk')      
ax.legend()                                     

plt.show()

