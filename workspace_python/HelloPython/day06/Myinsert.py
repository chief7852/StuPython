
from day06 import MysqlConfig

conn = MysqlConfig.conn

col01 = input("col01에 넣을값을 입력하십시오 >")
col02 = input("col02에 넣을값을 입력하십시오 >")
col03 = input("col03에 넣을값을 입력하십시오 >")
try:
    sql = f"insert into sample(col01 ,col02 ,col03) values ({col01},{col02},{col03})"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print(cur.rowcount)
    
finally:
    cur.close()
    conn.close()