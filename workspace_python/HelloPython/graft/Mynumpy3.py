import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np               
import matplotlib.pyplot as plt
import numpy as np
import pymysql
from graft import ColNum, ColName, MysqlConfig
import re

num = ColNum.numnum()
name =ColName.colName()

print(num)
print(name)


def getPrices(s_name):
    arr = []
    
    conn = MysqlConfig.conn
    curs = conn.cursor()
    
    
    sql = "SELECT s000020 FROM stock_sync_0121;"
    curs.execute(sql, s_name)
    rows = curs.fetchall()
    
    for i in rows:
        tmp =int(re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',str(i)))
        arr.append(tmp)
    print(rows)
    
    
    conn.close()
    return arr

mpl.rcParams['legend.fontsize'] = 10            

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.zeros(119)

y = range(119)
zs = []

for i in name:
    zs.append(getPrices(f"{i}"))
# zs.append(getPrices("삼성전자"))
# zs.append(getPrices("LG"))
# zs.append(getPrices("SK"))        

ax.plot(x+0, y, zs[0], label='SAMSUNG')
ax.plot(x+1, y, zs[1], label='LG')
ax.plot(x+2, y, zs[2], label='SK')

ax.legend()                                       

plt.show()