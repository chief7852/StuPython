import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np               
import matplotlib.pyplot as plt
import numpy as np
import pymysql

def getPrices(s_name):
    arr = []
    conn = pymysql.connect(
        user='root', 
        passwd='python', 
        host='127.0.0.1', 
        db='python', 
        charset='utf8'
    )
    curs = conn.cursor()
    
    sql = """
            SELECT s_code, s_name, s_price, in_date
            FROM stock
            WHERE s_name = %s
          """
    curs.execute(sql, s_name)
    rows = curs.fetchall()
    print(rows)
    
    frist_price = rows[0][2]
    print("frist_price", frist_price)
    for row in rows:
        arr.append(row[2]/frist_price)
        
    conn.close()
    return arr

mpl.rcParams['legend.fontsize'] = 10            

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.zeros(119)

y = range(119)
zs = []

zs.append(getPrices("삼성전자"))
zs.append(getPrices("LG"))
zs.append(getPrices("SK"))        

ax.plot(x+0, y, zs[0], label='SAMSUNG')
ax.plot(x+1, y, zs[1], label='LG')
ax.plot(x+2, y, zs[2], label='SK')

ax.legend()                                       

plt.show()