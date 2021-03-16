import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'python',
    db='python',
    charset='utf8'
    )