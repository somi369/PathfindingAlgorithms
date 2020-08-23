from tkinter import Label
from tkinter import Tk
from tkinter import Menu
from tkinter import Button
from time import sleep
from collections import defaultdict

#Root
root = Tk()
root.title('Pathfinding Algorithms')
root.geometry("800x600")

#Global variables
cursorType = 2
myButtons = defaultdict(list)
n = 10

#Menubar click functions
def StartNodeClick():
    global cursorType
    cursorType = 0     
def EndNodeClick():
    global cursorType
    cursorType = 1    
def WallNodeClick():
    global cursorType
    cursorType = 2
def NormalNodeClick():
    global cursorType
    cursorType = 3
def ClearWallNodeClick():
    global n
    for row in range(0,n):
        for column in range(0,n):
            if myButtons[row][column]["background"] == "black":
                myButtons[row][column].config(bg="white")

def StartClick():
    DijkstraAlg()
    pass



#Menubar area
menubar = Menu(root)
root.config(menu=menubar)
#
algorithmMenu = Menu(menubar)
menubar.add_cascade(label='Algorithms', menu=algorithmMenu) 
algorithmMenu.add_command(label='Dijkstra')
algorithmMenu.add_command(label='A*')
algorithmMenu.add_command(label='Breadth First Search')
algorithmMenu.add_command(label='Depth First Search')
#
nodeMenu = Menu(menubar)
menubar.add_cascade(label='Nodes', menu=nodeMenu) 
nodeMenu.add_command(label='Start node', command=StartNodeClick)
nodeMenu.add_command(label='End node', command=EndNodeClick)
nodeMenu.add_command(label='Wall node', command=WallNodeClick)
nodeMenu.add_command(label='Clear Wall nodes', command=ClearWallNodeClick)
#
menubar.add_command(label="Start", command=StartClick)

#Button Grid functions etc


def ClearStartNode():
    global n
    for row in range(0,n):
        for column in range(0,n):
            if myButtons[row][column]["background"] == "orange":
                myButtons[row][column].config(bg="white")

def ClearEndNode():
    global n
    for row in range(0,n):
        for column in range(0,n):
            if myButtons[row][column]["background"] == "yellow":
                myButtons[row][column].config(bg="white")

def OnButtonClick(r,c):
    global cursorType
    if cursorType == 0 and myButtons[r][c]["background"] != "yellow":
        #Start Node mode
        ClearStartNode()
        myButtons[r][c].config(bg="orange")
    elif cursorType == 1 and myButtons[r][c]["background"] != "orange":
        #End Node mode
        ClearEndNode()
        myButtons[r][c].config(bg="yellow")
    elif cursorType == 2 and myButtons[r][c]["background"] != "yellow" and myButtons[r][c]["background"] != "orange":
        #Wall Node mode
        myButtons[r][c].config(bg="black")
    
for row in range(0,n):
    for column in range(0,n):
        mybutton = Button(root,bg="white",height=1,width=2,command=lambda row=row , column=column: OnButtonClick(row,column))
        myButtons[row].append(mybutton)
        mybutton.grid(row=row,column=column,padx=1,pady=1)

#Default start node
myButtons[0][0].config(bg="orange")
#Default end node
myButtons[n-1][n-1].config(bg="yellow")



#bejárt elemek listája
#bejárandó
#rekurzívan amíg meg nem találja a célt
#útvonal?
def DijkstraAlg():
    #create matrix
    addressMatrix = defaultdict(list)
    for row in range(0,n):
        for column in range(0,n):
            if myButtons[row][column]["background"] == "orange":
                tempstr = str(row)+','+str(column)
                tempList = ['Start',tempstr]
                addressMatrix[row].append(tempList)
            elif myButtons[row][column]["background"] == "yellow":
                tempstr = str(row)+','+str(column)
                tempList = ['End',tempstr]
                addressMatrix[row].append(tempList)
            elif myButtons[row][column]["background"] == "black":
                tempstr = str(row)+','+str(column)
                tempList = ['Wall',tempstr]
                addressMatrix[row].append(tempList)
            else:
                tempstr = str(row)+','+str(column)
                tempList = ['Normal',tempstr]
                addressMatrix[row].append(tempList)
    #updating list
    print(addressMatrix)

    # foundEnd = False
    # NextNodes

    #while(!foundEnd&&len(nextNodes)!=0)
        #nextNodes -> blue color indicates these are checked
        #get nextNodes
        #nextNodes -> lightblue color to indicate these are coming



    # print(addressMatrix)
    # addressMatrix[0][0].append("kekw")
    # print(addressMatrix[0][0])

# valami()
root.mainloop()