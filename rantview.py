from tkinter import *
import api
import profileview

api = api.api()
class viewrant:
    rant = ""
    def __init__(self, master,rant):
        self.rant = rant
        frame = Frame(master)
        frame.pack()

        frame2 = Frame(frame)
        frame2.pack(side=RIGHT)
        score = Label(frame, text=rant["rant"]["score"])
        w = Label(frame, text=rant["rant"]["text"], wraplength=200)
        score.pack(side=LEFT)
        w.pack(side=LEFT)
        self.upv = Button(frame2, text="++", command=self.u)
        self.upv.pack()
        self.dv = Button(frame2, text="--", command=self.d)
        self.dv.pack()
        self.pr = Button(frame2, text="Profile", command=self.openprofile)
        self.pr.pack()

    def u(self):
        print("++")

    def d(self):
        print("--")

    def openprofile(self):
        profileroot = Toplevel()
        rantapp = profileview.profileview(profileroot,api.get_user(self.rant["rant"]["user_id"]))
        profileview.mainloop()
