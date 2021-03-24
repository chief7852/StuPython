from flask import Flask
from flask.templating import render_template
from day12.Mydao import MyEmpDao
from flask.globals import request
app = Flask(__name__)
 
@app.route("/emp")
def emp():
    list = MyEmpDao().getEmps()
    return render_template("emp.html",list=list)

@app.route("/test")
def ajax():
    arr = []
    sabun = request.args.get('sabun')
    print(sabun)
    arr = MyEmpDao().selEmps(sabun)
    print(arr)
    
    
if __name__ == "__main__":
    app.run(host='localhost', port=80, debug=True)

