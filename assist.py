import requests as r
from bs4 import BeautifulSoup
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
        html = r.get(self.url,cookies=self.cookie).text
        strippedHtml = html.replace(" ","")
        if "initYoutubePlayer(containerId, videoId, thumbnailSrc, topOverlayText)" in html:
            start = strippedHtml.find("letvideoId") + 12
            end = start + 11
            videoId = strippedHtml[start:end]
            print(videoId)
            return "https://www.youtube.com/watch?v=" + videoId 
        elif "data-youtube-video" in html:
            start = strippedHtml.find("data-youtube-video") + len("data-youtube-video") + 2 # for = and "
            end = start + 11
            videoId = strippedHtml[start:end]
            print(videoId)
            return "https://www.youtube.com/watch?v=" + videoId 
        else:
            soup = BeautifulSoup(html,"html.parser")
            link = soup.find("video",attrs={"id":"video_1"}).find("source").get("src")
            return link
