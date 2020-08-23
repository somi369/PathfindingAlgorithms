from tkinter import Label
from tkinter import Tk
from tkinter import Menu
from tkinter import Button
from time import sleep
from collections import defaultdict

#active background
#clear walls
#reset

#root area
root = Tk()
root.title('Pathfinding Algorithms')
root.geometry("800x600")

cursorType = 3

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

def StartClick():
    pass


#Menu area
menubar = Menu(root)
root.config(menu=menubar)
#Algorithms Tab
algorithmMenu = Menu(menubar)
menubar.add_cascade(label='Algorithms', menu=algorithmMenu) 
algorithmMenu.add_command(label='Dijkstra')
algorithmMenu.add_command(label='A*')
algorithmMenu.add_command(label='Breadth First Search')
algorithmMenu.add_command(label='Depth First Search')
#Node Tab
nodeMenu = Menu(menubar)
menubar.add_cascade(label='Nodes', menu=nodeMenu) 
nodeMenu.add_command(label='Start node', command=StartNodeClick)
nodeMenu.add_command(label='End node', command=EndNodeClick)
nodeMenu.add_command(label='Wall node', command=WallNodeClick)
nodeMenu.add_command(label='Normal node', command=NormalNodeClick)
#
menubar.add_command(label="Start", command=StartClick)






#Adding stuff to GUI




myButtons = defaultdict(list)

def OnButtonClick(r,c):
    global cursorType
    if cursorType == 0:
        #Start Node mode
        myButtons[r][c].config(bg="green")
    elif cursorType == 1:
        #End Node mode
        myButtons[r][c].config(bg="yellow")
    elif cursorType == 2:
        #Wall Node mode
        myButtons[r][c].config(bg="black")
    else:
        #cursorType == 3:
        #Normal Node mode
        myButtons[r][c].config(bg="white")
    


for row in range(0,10):
    for column in range(0,10):
        mybutton = Button(root,bg="white",height=1,width=2,command=lambda row=row , column=column: OnButtonClick(row,column))
        myButtons[row].append(mybutton)
        mybutton.grid(row=row,column=column,padx=1,pady=1)

# idx = 0
# def valami():
#     global idx
#     aLabel = myButtons[0][idx].config(bg="blue")
#     idx += 1
#     root.after(1000,valami)



    

#Default start node
myButtons[0][0].config(bg="green")
#Default end node
myButtons[9][9].config(bg="yellow")





# valami()
root.mainloop()