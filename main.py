## Instagram image/video downloader
## Created by Pranav Sricharan
## For bugs please report to pranav.sricharan@gmail.com
## Enjoy using this application
import urllib.request
import re
from InstagramPost import InstagramPost
from InstagramProfile import InstagramProfile

# Open GUI mode if GTK exists or open CLI mode
if __name__ == '__main__':
    try:
        import gi
        gi.require_version('Gtk', '3.0')
        from gi.repository import Gtk,Gdk

        class MyWindow(Gtk.Window):

            def __init__(self):
                builder = Gtk.Builder()
                builder.add_from_file("gui/window.glade")
                builder.connect_signals(self)
                window = builder.get_object("window1")
                self.statusLabel = builder.get_object("statusLabel")
                self.urlTxt = builder.get_object("urlTxt")
                window.connect("delete-event", Gtk.main_quit)
                window.show_all()


            def downloadImg(self,widget):
                self.statusLabel.set_property("label","Checking URL..." )
                url = self.urlTxt.get_property("text")
                if "/p/" in url:
                    post = InstagramPost(url)
                    if post.getSuccess():
                        self.statusLabel.set_property("label","Found " + post.getType())
                        post.download()
                        self.statusLabel.set_property("label","Saved at img/" + post.getFilename() + " of program directory")
                    else:
                        self.statusLabel.set_property("label","Error! Please make sure that the URL you've entered is valid or a public instagram post")
                else:
                    username = url.strip('/')
                    username = username[username.rfind('/')+1:]
                    self.statusLabel.set_property("label","Checking username " + username)
                    profile = InstagramProfile(username)
                    self.statusLabel.set_property("label","Downloading at img/" + username + " of program directory")
                    profile.download()
                    self.statusLabel.set_property("label","Download complete at img/" + username + " of program directory")

        win = MyWindow()
        Gtk.main()

    except ImportError:
        print("Instagram image/video downloader")
        print("Developed by @pranavsricharan")
        print()
        ch = 'y'
        while ch == 'y':
            url = input("Enter an Instagram url: ")
            if "/p/" in url:
                post = InstagramPost(url)
                while not post.getSuccess():
                    print("\n"*3 + "OOPS...Something went wrong...")
                    print("The URL you entered doesn't seem to be valid... Please make sure that the URL you've entered is valid or a public instagram post")
                    url = input("Enter a valid Instagram public url: ")
                    post = InstagramPost(url)

                print("Found",post.getType())
                post.download()
                print("Saved at img/", post.getFilename(), "of program directory")

            else:
                username = url.strip('/')
                username = username[username.rfind('/')+1:]
                profile = InstagramProfile(username)
                profile.download()

            ch = input("Another image? (y/n): ")
            ch = ch.lower()
        x = input("Press return to exit")
