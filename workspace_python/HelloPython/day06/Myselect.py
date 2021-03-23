
from day06 import MysqlConfig
arr = []
conn = MysqlConfig.conn

sql = 'SELECT * FROM stock WHERE s_name = "삼성전자" ORDER BY in_date asc;'
cur = conn.cursor()
cur.execute(sql)
arr = cur.fetchall()
print(len(arr))