from tkinter import *
from time import sleep

root = Tk()


cursorType = 0

myLabel = Label(root,text=cursorType)

def SelectAlgorithmBTNClick():
    global cursorType
    cursorType = 4   
def StartNodeBTNClick():
    global cursorType
    cursorType = 0     
    myLabel.config(text=str(cursorType))
def EndNodeBTNClick():
    global cursorType
    cursorType = 1    
    myLabel.config(text=str(cursorType))
def WallNodeBTNClick():
    global cursorType
    cursorType = 2     
    myLabel.config(text=str(cursorType))

selectAlgorithmBTN = Button(root,text="Select algorythm",command=SelectAlgorithmBTNClick)
startNodeBTN = Button(root,text="Start Node",command=StartNodeBTNClick)
endNodeBTN = Button(root,text="End Node",command=EndNodeBTNClick)
wallNodeBTN = Button(root,text="Wall Node",command=WallNodeBTNClick)


selectAlgorithmBTN.grid(row=0,column=0)
startNodeBTN.grid(row=0,column=1)
endNodeBTN.grid(row=0,column=2)
wallNodeBTN.grid(row=0,column=3)

myLabel.grid(row=0,column=4)

#sleep(1)


root.mainloop()