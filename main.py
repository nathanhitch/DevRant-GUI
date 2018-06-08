from tkinter import *
import api
import rantview
rantroot = ""
ind = 0
rantlist = []
class App:
    api = api.api()
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.scrollbar = Scrollbar(frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)


        self.listbox = Listbox(frame, yscrollcommand=self.scrollbar.set)
        rants = self.api.get_rants()
        for i in rants["rants"]:
            global rantlist
            self.listbox.insert(END,i["text"].encode())
            self.listbox.pack(side=TOP, fill=BOTH)
            rantlist.append(i["id"])
        self.scrollbar.config(command=self.listbox.yview)
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="View", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        global ind
        global rantroot
        ind = self.listbox.curselection()[0]
        rant = self.api.get_rant(str(rantlist[ind]))
        rantroot = Toplevel()
        rantapp = rantview.viewrant(rantroot,rant)
        rantroot.mainloop()


root = Tk()

app = App(root)

root.mainloop()