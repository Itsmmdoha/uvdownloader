from flask import Flask,request,render_template, make_response
from assist import User
app = Flask(__name__)

@app.route("/")
def home():
    if request.cookies.get("creds"):
        r = render_template("logged_in.html")
    else:
        r = render_template("index.html")
    return r
@app.route("/data",methods=["POST"])
def data():
    try:
        if request.cookies.get("creds"):
            cookie = request.cookies.get("creds")
            creds = cookie.split(":")
            reg = creds[0]
            password = creds[1]
        else:
            reg = request.form["reg"]
            password = request.form["password"]

        url = request.form["url"]
        target = User(url,reg,password)
        valid = target.login()
        if valid:
            response = make_response()
            response.set_cookie("creds",f"{reg}:{password}",domain=request.host)
            url = target.getVidLink()
            response.content_type = "text/html"
            response.data = render_template("redirect.html",link = url)
            return response 
        else:
            response = make_response()
            response.delete_cookie("creds")
            response.data = render_template("invalid.html")
            response.content_type = "text/html"
            return response
    except:
        return render_template("invalid.html") 

if __name__=="__main__":
    app.run(debug=True)
