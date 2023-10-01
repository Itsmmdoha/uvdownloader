import requests as r
class User:
    cookie = {} 
    def __init__(self,url,reg,password):
        self.url = url
        self.reg = reg 
        self.password = password
    def login(self):
        url = "https://online.udvash-unmesh.com/Account/Login"
        data = {
                "RegistrationNumber":self.reg,
                "Password":self.password
                }
        login_res = r.post(url,data=data,allow_redirects=False)
        if "Invalid" in login_res.text:
            return False
        else:
            cookie_string = login_res.headers["set-cookie"][10:]
            self.cookie[".ASPXAUTH"] = cookie_string
            return True
    def getVidLink(self):
        res = r.get(self.url,cookies=self.cookie).text
        start = res.find("let videoId") + 15
        end = start + 11
        return "https://www.youtube.com/watch?v=" + res[start:end]

