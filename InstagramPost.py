import urllib.request
import re
import os

class InstagramPost:

    def __init__(self,url):
        self.url = url
        self.filename = None
        self.collectData()
        self.subFolderPath = None

    def setSubFolder(self, dirName):
        self.subFolderPath = dirName

    def collectData(self):
        try:
            data = urllib.request.urlopen(self.url)
            data = data.read()
            data = str(data)

            # Find video URL
            regex = ".*?<meta property=\"og:video[^:]??\" content=\"(.*?)\".*?\" />"
            self.imageUrl = re.match(regex,data)

            # Check if any video exists
            if(self.imageUrl is not None):
                self.type = "Video"
            else:
                regex = ".*?<meta property=\"og:image[^:]??\" content=\"(.*?)\".*?\" />"
                self.imageUrl = re.match(regex,data)
                self.type = "Image"

            self.success = False if(self.imageUrl is None) else True
            self.imageUrl = self.imageUrl.group(1)

            # Get the file name from the URL
            self.filename = re.match(".*?/([^/]*?\.*?)$",self.imageUrl)
            self.filename = self.filename.group(1)

        except urllib.error.HTTPError:
            self.success = False

        return self.success


    def download(self):
        # Open URL and get image contents
        attempts = 0
        image = None

        while image is None and attempts < 3:
            if attempts != 0:
                print("Retry[{}]: {}".format(attempts, self.imgUrl))
            image = urllib.request.urlopen(self.imageUrl)
            image = image.read()
            attempts += 1

        # Save the image to local file
        dirPath = os.path.dirname(os.path.realpath(__file__))
        dirPath = os.path.join(dirPath,'img')
        if self.subFolderPath is not None:
            dirPath = os.path.join(dirPath,self.subFolderPath)
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)
        file = open(os.path.join(dirPath,self.filename), "wb")
        file.write(image)
        file.close()


    def getSuccess(self):
        return self.success


    def getFilename(self):
        return self.filename


    def getType(self):
        return self.type
