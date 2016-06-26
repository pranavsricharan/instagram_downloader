## Instagram image downloader
## Created by Pranav Sricharan
## For bugs please report to pranav.sricharan@gmail.com
## Enjoy using this application
import urllib.request
import re
print("Instagram image downloader")
print("Developed by @pranavsricharan")
print()
ch = 'y'
while ch == 'y':
    url = input("Enter an Instagram url: ")
    data = urllib.request.urlopen(url)
    data = data.read()
    data = str(data)
    regex = ".*?<meta property=\"og:image\" content=\"(.*?)\?.*?\" />.*?"
    imageUrl = re.match(regex,data)
    imageUrl = imageUrl.group(1)
    print("Found image:",imageUrl)
    image = urllib.request.urlopen(imageUrl)
    image = image.read()
    filename = re.match(".*?/([^/]*?\.jpg)$",imageUrl)
    filename = filename.group(1)
    file = open("img/"+filename,"wb")
    file.write(image)
    file.close()
    print("File saved at:","img/"+filename,"of program directory")
    ch = input("Another image? (y/n): ")
    ch = ch.lower()
x = input("Press return to exit")
