import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np               
import matplotlib.pyplot as plt
from graft import ColNum, ColName, MysqlConfig
from win32comext.mapi.mapiutil import GetAllProperties
import pymongo




def getPrices(s_name):
    
    arr = []
    connection = pymongo.MongoClient("mongodb://localhost:27017/")
    db = connection.pyhon
    
    stock = db.stock
    
    rows = stock.find({'s_name':s_name}).sort('in_date',1)
    first_price = rows[0]['s_price']
    for r in rows:
        int_s_price = int(r['s_price'])/int(first_price)
        arr.append(int_s_price)
        return arr


mpl.rcParams['legend.fontsize'] = 10            

fig = plt.figure()
ax = fig.gca(projection='3d')

zs = []
x = np.zeros(10)

y = range(10)

zs.append(getPrices("삼성전자"))
zs.append(getPrices("LG"))
zs.append(getPrices("SK")) 

print(len(zs))

ax.plot(x+0, y, zs[0], label='SAMSUNG')
ax.plot(x+1, y, zs[1], label='LG')
ax.plot(x+2, y, zs[2], label='SK')
ax.legend()                                       

plt.show()