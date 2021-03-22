from graft import MysqlConfig
from win32comext.mapi.mapiutil import GetAllProperties

conn = MysqlConfig.conn



def getAllPrices():
    zs = []
    sql = """
    select s000020, s000040, s000050 
    from stock_sync_0121
    LIMIT 10;
    """
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    
    cnt10 = len(rows)
    cnt3 = len(rows[0])
    
    for i3 in range(cnt3):
        line = []
        first_price = rows[0][i3]
        for j10 in range(cnt10):
            line.append(rows[j10][i3]/first_price)
        zs.append(line)

    conn.close()    
    return(zs)
if __name__ == '__main__':
    arr = GetAllProperties()
    print(arr)