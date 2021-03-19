from graft import MysqlConfig
def numnum():

    
    conn = MysqlConfig.conn
    
    
    sql="""
        SELECT COUNT(*) 
        FROM information_schema.columns 
        WHERE table_name='stock_sync_0121'
        """
    cur = conn.cursor()
    cur.execute(sql)
    aa =cur.fetchall()
    num =str(aa).replace("(","").replace(")","").replace(",","")
    
    return int(num)