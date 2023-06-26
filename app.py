from flask import Flask,request,render_template,redirect
from assist import User
app = Flask(__name__)

@app.route("/")
def home():
    r = render_template("index.html")
    return r
@app.route("/data",methods=["POST"])
def data():
    try:
        url = request.form["url"]
        reg = request.form["reg"]
        password = request.form["password"]
        target = User(url,reg,password)
        valid = target.login()
        if valid:
            url = target.getVidLink()
            return redirect(url,code=302)
        else:
            return render_template("invalid.html") 
    except:
        return render_template("invalid.html") 

