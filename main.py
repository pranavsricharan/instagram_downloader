## Instagram image/video downloader
## Created by Pranav Sricharan
## For bugs please report to pranav.sricharan@gmail.com
## Enjoy using this application
import urllib.request
import re
print("Instagram image/video downloader")
print("Developed by @pranavsricharan")
print()
ch = 'y'
while ch == 'y':
    url = input("Enter an Instagram url: ")
    data = urllib.request.urlopen(url)
    data = data.read()
    data = str(data)
    # Find video URL
    regex = ".*?<meta property=\"og:video[^:]??\" content=\"(.*?)\".*?\" />"
    imageUrl = re.match(regex,data)
    # Check if any video exists
    if(imageUrl is not None):
        imageUrl = imageUrl.group(1)
        print("Found video:",imageUrl)
        # Open and get the contents of the video
        image = urllib.request.urlopen(imageUrl)
        image = image.read()
        # Get the file name from the URL
        filename = re.match(".*?/([^/]*?\.*?)$",imageUrl)
        filename = filename.group(1)
        # Save the video to the local file
        file = open("img/"+filename,"wb")
        file.write(image)
        file.close()
        print("File saved at:","img/"+filename,"of program directory")
    else: # If the URL is not a video
        #Find the image URL
        regex = ".*?<meta property=\"og:image\" content=\"(.*?)\?.*?\" />.*?"
        imageUrl = re.match(regex,data)
        # Check if any image exists
        if(imageUrl is not None):
            imageUrl = imageUrl.group(1)
            print("Found image:",imageUrl)
            # Open URL and get image contents
            image = urllib.request.urlopen(imageUrl)
            image = image.read()
            # Get the file name from the URL
            filename = re.match(".*?/([^/]*?\.jpg)$",imageUrl)
            filename = filename.group(1)
            # Save the image to local file
            file = open("img/"+filename,"wb")
            file.write(image)
            file.close()
            print("File saved at:","img/"+filename,"of program directory")
        else:
            print("Some error occured...")
    ch = input("Another image? (y/n): ")
    ch = ch.lower()
x = input("Press return to exit")
