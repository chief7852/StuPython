from flask.globals import request
from flask import Flask
from smsAPI.SMSAPI import testingsms
app = Flask(__name__)
 
@app.route("/32")
def hello():
    phone = request.args.get('phone')
    text = request.args.get('text')
    result = testingsms(phone,text)
    return result
 
if __name__ == "__main__":
    app.run(host='localhost', port=80, debug=True)

