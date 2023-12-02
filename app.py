from flask import Flask,request,render_template, make_response
from assist import User
app = Flask(__name__)

@app.route("/")
def home():
    if request.cookies.get("creds"):
        response = make_response()
        response.content_type = "text/html"
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.data = render_template("logged_in.html")
    else:
        response = make_response()
        response.content_type = "text/html"
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.data = render_template("index.html")
    return response
@app.route("/data",methods=["POST"])
def data():
    try:
        if request.cookie.get("Restricted"):
            return render_template("error.html",error_message="You are limited to download a video every 6 hours, try downlod this video after 6 hours of your last download. We are setting this rate limit feature to prevent piracy.")
        elif request.cookies.get("creds"):
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
            response.set_cookie("Restricted","True",domain=request.host,max_age=3600*6)
            url = target.getVidLink()
            response.content_type = "text/html"
            response.data = render_template("redirect.html",link = url)
            return response 
        else:
            response = make_response()
            response.delete_cookie("creds")
            response.data = render_template("invalid.html",error_message="Invalid Input")
            response.content_type = "text/html"
            return response
    except:
        return render_template("invalid.html") 

if __name__=="__main__":
    app.run(debug=True)
