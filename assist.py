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
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
        login_res = r.post(url,data=data,headers=headers,allow_redirects=False)
        if "Invalid" in login_res.text:
            return False
        else:
            cookie_string = login_res.headers["set-cookie"][10:]
            self.cookie[".ASPXAUTH"] = cookie_string
            return True
    def getVidLink(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
        html = r.get(self.url,cookies=self.cookie,headers=headers).text
        strippedHtml = html.replace(" ","")
        if "initYoutubePlayer(containerId, videoId, thumbnailSrc, topOverlayText)" in html:
            start = strippedHtml.find("letvideoId") + 12
            end = start + 11
            videoId = strippedHtml[start:end]
            print(videoId)
            return "https://www.youtube.com/watch?v=" + videoId 
        elif "data-youtube-video" in html: #youtube link extraction in current layout
            start = strippedHtml.find("data-youtube-video") + len("data-youtube-video") + 2 # for = and "
            end = start + 11
            videoId = strippedHtml[start:end]
            print(videoId)
            return "https://www.youtube.com/watch?v=" + videoId 
        elif "data-all-video-source" in html: #aws s3 bucket link extraction
            print("detected")
            soup = BeautifulSoup(html, 'html.parser')
            video_link = soup.select_one('li[data-id="1"]')['data-all-video-source']
            return video_link
        else:
            soup = BeautifulSoup(html,"html.parser")
            link = soup.find("video",attrs={"id":"video_1"}).find("source").get("src")
            return link
