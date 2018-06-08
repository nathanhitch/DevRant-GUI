from tkinter import *
import webbrowser
class profileview:
    user = ""
    def __init__(self, master,user):
        self.user = user
        frame = Frame(master)
        frame.pack()
        master.title(user["profile"]["username"])
        score = Label(frame, text=user["profile"]["score"])
        score.pack(side=LEFT)
        about = Label(frame, text=user["profile"]["about"])
        about.pack(side=TOP)
        skills = Label(frame, text="skills: "+user["profile"]["skills"])
        skills.pack()
        if not user["profile"]["website"] == '':
            self.website = Button(frame, text=user["profile"]["website"], command=self.openwebsite)
            self.website.pack(side=BOTTOM)
    def openwebsite(self):
        url = self.user["profile"]["website"]
        if not url[:4] == "http":
            url = "http://" + url
        webbrowser.open(url)