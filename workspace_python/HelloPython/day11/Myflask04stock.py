import pymysql
from flask import Flask,render_template
from day06 import MysqlConfig
from flask.globals import request

app = Flask(__name__)

def stocked(temp):
    arr =[]
    conn = MysqlConfig.conn
    
    sql = f'SELECT s_code,s_name,s_price,in_date FROM stock WHERE s_name = "{temp}" ORDER BY in_date asc;'
    cur = conn.cursor()
    cur.execute(sql)
    arr = cur.fetchall()
    print(arr[0][0])
    return arr

@app.route("/para")
def hello():
    return render_template("stock.html")

@app.route("/search",methods = ['post','get'])
def search():
    brand = []
    temp = request.args.get('name', "")
    brand = stocked(temp)
    print(brand)
    return render_template("stock.html",val = brand)


    return temp
if __name__ == "__main__":
    app.run(host='localhost', port=80, debug=True)
