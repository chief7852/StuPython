from flask import Flask
from flask import request
app = Flask(__name__)
 
@app.route("/param",methods = ['post','get'])
def hello():
    temp = request.args.get('a', "하하하")
    temp1 = request.args.get('juso', "서울시")
    if request.method == 'POST':
        temp = request.form.get('a')
        return temp
    return temp + "-" + temp1


    return temp
if __name__ == "__main__":
    app.run(host='localhost', port=80, debug=True)
