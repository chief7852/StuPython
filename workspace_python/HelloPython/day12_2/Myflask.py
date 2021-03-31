from flask import Flask,render_template,request,jsonify
from day12_2.mydao import MyEmpDao

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/")
@app.route("/emp")
def emp():
    list = MyEmpDao().getEmps()  
    return render_template('emp.html',list=list)   

@app.route('/ins.ajax', methods=['POST'])
def ins_ajax():
    data = request.get_json()
    sabun   = data['sabun']
    name    = data['name']
    dept    = data['dept']
    mobile  = data['mobile']
    cnt  = MyEmpDao().insEmp(sabun, name, dept, mobile)
    result = "fail"
    if cnt == 1 :
        result = "success"
    
    return jsonify(result = result)                

if __name__ == "__main__":              
    app.run(host="127.0.0.1", port="80")