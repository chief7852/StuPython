import re
from graft import MysqlConfig

conn = MysqlConfig.conn


sql = "SELECT s000020 FROM stock_sync_0121;"
cur = conn.cursor()
cur.execute(sql)
arr = cur.fetchall()



for i in arr:
    print(re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',str(i)))