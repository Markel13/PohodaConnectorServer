from tkinter import *

import urllib.request

class CallPHPClass:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Call PHP script", command=self.callPHP)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):


        print("Call PHP from class")

    def callPHP(self):
        result = urllib.request.urlopen("http://www.istraka.cz/").read()
        print(result)


root = Tk()
p = CallPHPClass(root)


#theLabel = Label(root, text="This is my text")
#theLabel.pack()

#theButton = Button(root,text="Call php script")
#theButton.bind("<Button-1>", callPHP())
#theButton.pack(side=TOP)
#theButton.bind()

root.mainloop()
