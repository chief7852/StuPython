import pymysql

conn = pymysql.connect(
    user='root', 
        passwd='python', 
        host='127.0.0.1', 
        db='python', 
        charset='utf8'
    )