import pymysql

conn = pymysql.connect(
    user='root', 
        passwd='python', 
        host='127.0.0.1', 
        db='_stock_old', 
        charset='utf8'
    )