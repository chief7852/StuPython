from day06 import MysqlConfig

conn = MysqlConfig.conn

dele = input("삭제하고싶은 문자를 선택하십시오")

try:
    sql = f"delete from sample where col01='{dele}'"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print(cur.fetchall())
finally:
    cur.close()
    conn.close()