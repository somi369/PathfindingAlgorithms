from tkinter import *
from time import sleep
from collections import defaultdict



# def __init__(self, root):
#     Frame.__init__(self,root)
#     self.grid()
#     self.mychosenattribute=8 
#     self.create_widgets()

#root area
root = Tk()
root.title('Pathfinding Algorithms')
root.geometry("800x600")


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
def StartBTNClick():
    global cursorType
    cursorType = 2     
    myLabel.config(text=str(cursorType))



#Algorythm
algorythmOptions = [
    "Dijkstra's",
    "A*",
    "Breadth First Search",
    "Depth First Search"
]

algorithm = StringVar()
algorithm.set(algorythmOptions[0])



selectAlgorithmDROP = OptionMenu(root, algorithm, *algorythmOptions )
#selectAlgorithmBTN = Button(root,text="Select algorythm",command=SelectAlgorithmBTNClick)
startNodeBTN = Button(root,text="Start Node",command=StartNodeBTNClick)
endNodeBTN = Button(root,text="End Node",command=EndNodeBTNClick)
wallNodeBTN = Button(root,text="Wall Node",command=WallNodeBTNClick)
startBTN = Button(root,text="Start",command=StartBTNClick)


#Adding stuff to GUI

# selectAlgorithmDROP.grid(row=0,column=0)
# startNodeBTN.grid(row=0,column=1)
# endNodeBTN.grid(row=0,column=2)
# wallNodeBTN.grid(row=0,column=3)
# startBTN.grid(row=0,column=4)
# myLabel.grid(row=0,column=4)

# self.mybuttons = defaultdict(list)
# for rows in range(1,21):
#     for columns in range(1,21):
#         self.mybuttons[rows].append(Button(self, text=''))

myLabels = defaultdict(list)

for row in range(10):
    for column in range(10):
        label = Label(root,bg="white",height=1,width=2)
        myLabels[row].append(label)
        label.grid(row=row,column=column,padx=1,pady=1)

idx = 0
def valami():
    global idx
    aLabel = myLabels[0][idx].config(bg="blue")
    idx += 1
    root.after(1000,valami)

valami()
root.mainloop()