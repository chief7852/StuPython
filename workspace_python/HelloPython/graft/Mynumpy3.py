import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np               
import matplotlib.pyplot as plt
from graft import ColNum, ColName, MysqlConfig
from win32comext.mapi.mapiutil import GetAllProperties




def getAllPrices():
    conn= MysqlConfig.conn
    
    zs = []
    sql = """
    select *
    from stock_sync_0121
    
    """
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    
    cnt10 = len(rows)
    cnt3 = len(rows[0])-1
    
    for i3 in range(cnt3):
        line = []
        first_price = rows[0][i3]
        
        for j10 in range(cnt10):
            if first_price ==0:
                line.append(0.8)
            else:
                line.append(rows[j10][i3]/first_price)
        zs.append(line)

    conn.close()    
    return(zs)

mpl.rcParams['legend.fontsize'] = 10            

fig = plt.figure()
ax = fig.gca(projection='3d')

zs = getAllPrices()
x = np.zeros(len(zs[0]))

y = range(len(zs[0]))



print(len(zs))

for i in range(len(zs)):
    ax.plot(x+i , y, zs[i])
  

ax.legend()                                       

plt.show()