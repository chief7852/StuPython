
from day06 import MysqlConfig

conn = MysqlConfig.conn



try:
    sql = 'select col01,col02,col03 from sample';
    cur = conn.cursor()
    cur.execute(sql)
    print(cur.fetchall())
finally:
    cur.close()
    conn.close()