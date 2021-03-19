import re
def colName():
    from graft import MysqlConfig
    conn = MysqlConfig.conn
    
    sql="""
        SELECT column_name
        FROM information_schema.columns 
        WHERE table_name='stock_sync_0121';
        """
    cur = conn.cursor()
    cur.execute(sql)
    arr = cur.fetchall()
    tt =[]
    for i in arr:
        if arr[0]:
            tt.append(re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',str(i)))
        
    return tt
    
    
