from InstagramPost import InstagramPost
import urllib.request
from urllib.error import HTTPError
import re
import json
import os
import multiprocessing as mp




class InstagramProfile:
    def __init__(self, username):
        self.username = username
        self.images = list()
        self.base_url = "http://www.instagram.com/" + self.username + "/"
        self.fetchImages()


    def fetchImages(self):
        hasNext = True
        url = self.base_url
        while hasNext:
            try:
                data = urllib.request.urlopen(url)
                data = data.read()
            except HTTPError as e:
                data = e.read()
                print(data)
            data = str(data)

            regex = ".*?window._sharedData = (.*?);</script>"
            jsonData = re.match(regex,data).group(1).strip()
            jsonData = jsonData.replace(r"\'", "'").replace("\\\\", '\\')

            jsonObject = json.loads(jsonData)
            media = jsonObject["entry_data"]["ProfilePage"][0]["user"]["media"]
            hasNext = media["page_info"]["has_next_page"]
            imageList = media["nodes"]

            lastId = None

            for image in imageList:
                lastId = image["id"]
                imgInfo = {'username': self.username, 'code': image["code"]}
                self.images.append(imgInfo)

            url = self.base_url + "?max_id=" + str(lastId)

    @staticmethod
    def downloadImg(imgInfo):
        try:
            imgUrl = "http://www.instagram.com/p/" + imgInfo["code"]
            post = InstagramPost(imgUrl)
            post.setSubFolder(imgInfo["username"])
            if post.collectData():
                post.download()
                print("Downloaded: ", imgInfo["code"])
        except Exception as e:
            print("[Error] Could not download", imgInfo["code"], e)


    def download(self):
        dirPath = os.path.dirname(os.path.realpath(__file__))
        dirPath = os.path.join(dirPath,'img')
        dirPath = os.path.join(dirPath,self.username)
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)
        pool = mp.Pool()
        pool.map(InstagramProfile.downloadImg, self.images)
