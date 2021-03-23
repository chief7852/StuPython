
from flask import Flask,render_template
app = Flask(__name__)
 
@app.route("/para")
def hello():
    list = ["홍길동","전우치","아토"]
    return render_template("list.html",a=list)
 
if __name__ == "__main__":
    app.run(host='localhost', port=80, debug=True)
