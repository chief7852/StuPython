from day12 import MysqlConfig
def selEmps(sabun):
        arr=[]
        conn = MysqlConfig.conn

        sql = f"SELECT sabun,e_name,dept,mobile FROM emp where sabun ={sabun}";
        cur = conn.cursor()
        cur.execute(sql)
        arr = cur.fetchall()
        print(arr)
        conn.close()
sabun = '1';        
selEmps(sabun)    
    