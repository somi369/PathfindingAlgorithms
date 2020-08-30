from tkinter import Label
from tkinter import Menu
from tkinter import Button
from tkinter import Tk
from time import sleep
from collections import defaultdict
from Node import NodeType
from Node import NodeStatus
from Node import Node
import copy
import threading
import time

class GUI:
    
    def __init__(self, sizeOfBoard, Tk):
        #Board size
        self._sizeOfBoard = sizeOfBoard
        #Tkinter
        self._root = Tk
        self._root.title('Pathfinding Algorithms')
        self._root.geometry("300x300") 
        #Menubar
        self._menubar = Menu(self._root)
        self._root.config(menu=self._menubar)
        #
        self._algorithmMenu = Menu(self._menubar)
        self._menubar.add_cascade(label='Algorithms', menu=self._algorithmMenu) 
        self._algorithmMenu.add_command(label='Dijkstra', command=self.SetToDijkstra)
        self._algorithmMenu.add_command(label='Depth First Search', command=self.SetToDFS)
        #
        self._nodeMenu = Menu(self._menubar)
        self._menubar.add_cascade(label='Nodes', menu=self._nodeMenu) 
        self._nodeMenu.add_command(label='Start node', command=self.StartNodeClick)
        self._nodeMenu.add_command(label='End node', command=self.EndNodeClick)
        self._nodeMenu.add_command(label='Wall node', command=self.WallNodeClick)
        self._nodeMenu.add_command(label='Clear nodes', command=self.ClearWallNodeClick)
        #
        self._menubar.add_command(label="Start", command=self.StartClick)
        #Etc
        self._cursorType = 2 
        self._algNum = 0
        self._myButtons = defaultdict(list)
        for row in range(0,self._sizeOfBoard):
            for column in range(0,self._sizeOfBoard):
                mybutton = Button(self._root,bg="white",height=1,width=2,command=lambda row=row , column=column: self.OnButtonClick(row,column))
                self._myButtons[row].append(mybutton)
                mybutton.grid(row=row,column=column,padx=1,pady=1)
        #Default start node
        self._myButtons[0][0].config(bg="orange")
        #Default end node
        self._myButtons[self._sizeOfBoard-1][self._sizeOfBoard-1].config(bg="yellow")
        #Start GUI
        #self.refresh()
        self._root.mainloop()
        

    ###Methods###

    def SetToDijkstra(self):
        self._algNum = 0
    
    def SetToDFS(self):
        self._algNum = 1    

    def StartNodeClick(self):
        self._cursorType = 0     

    def EndNodeClick(self):
        self._cursorType = 1    

    def WallNodeClick(self):
        self._cursorType = 2

    def NormalNodeClick(self):
        self._cursorType = 3

    def ClearWallNodeClick(self):
        for row in range(0,self._sizeOfBoard):
            for column in range(0,self._sizeOfBoard):
                if (self._myButtons[row][column]["background"] == "black" or 
                    self._myButtons[row][column]["background"] == "blue" or
                    self._myButtons[row][column]["background"] == "lightBlue" or
                    self._myButtons[row][column]["background"] == "green"):
                    self._myButtons[row][column].config(bg="white")

    def IsExploreableNode(self, nodeMatrix, row, column):

        if(row < 0 or row >= self._sizeOfBoard or column < 0 or column >= self._sizeOfBoard):
            return False
        elif(nodeMatrix[row][column].nodeStatus == NodeStatus.Unexplored and nodeMatrix[row][column].nodeType != NodeType.WallNode):
            return True
        else:
            return False

    def HasExploreableAdjacentNodes(self, nodeMatrix, row, column):
        if self.IsExploreableNode(nodeMatrix,row,column-1) or self.IsExploreableNode(nodeMatrix,row-1,column) or self.IsExploreableNode(nodeMatrix,row,column+1) or self.IsExploreableNode(nodeMatrix,row+1,column) :
            return True
        else:
            return False

    def DijkstraAlg(self):
        #Initialize nodeMatrix and Adding starting node to inQueue
        inQueueNodes = []
        nodeMatrix = defaultdict(list)
        for row in range(0,self._sizeOfBoard):
            for column in range(0,self._sizeOfBoard):
                nodeType = NodeType.NormalNode
                if self._myButtons[row][column]["background"] == "orange":
                    nodeType = NodeType.StartNode
                elif self._myButtons[row][column]["background"] == "yellow":
                    nodeType = NodeType.EndNode
                elif self._myButtons[row][column]["background"] == "black":
                    nodeType = NodeType.WallNode
                node = Node(row,column,nodeType,NodeStatus.Unexplored)
                nodeMatrix[row].append(node)
                if (node.nodeType == NodeType.StartNode):
                    node.nodeStatus=NodeStatus.Explored
                    inQueueNodes.append(node)
        if len(inQueueNodes) == 0:
            return False

        foundEndNode = False
        first = True
        finalNode = Node(-1,-1)
        while not foundEndNode and len(inQueueNodes)!=0 :
            time.sleep(0.3)
            #Color explored nodes
            if first:
                #dont need to color starting node
                first = False
            else:
                #Color InQueueNodes:
                for node in inQueueNodes:
                    self._myButtons[node.rowIdx][node.columnIdx].config(bg="blue")
                    nodeMatrix[node.rowIdx][node.columnIdx].nodeStatus=NodeStatus.Explored
            #Searching for new nodes
            newInQueueNodes = []
            for node in inQueueNodes:
                r0 = node.rowIdx
                r1 = node.rowIdx-1
                r2 = node.rowIdx+1
                c0 = node.columnIdx
                c1 = node.columnIdx-1
                c2 = node.columnIdx+1
                if (r1>=0 and 
                    nodeMatrix[r1][c0].nodeType!=NodeType.WallNode and
                    not(nodeMatrix[r1][c0] in newInQueueNodes) and 
                    nodeMatrix[r1][c0].nodeStatus!=NodeStatus.Explored):
                        nodeMatrix[r1][c0].previousNode = node
                        newInQueueNodes.append(nodeMatrix[r1][c0])
                if (r2<self._sizeOfBoard and
                    nodeMatrix[r2][c0].nodeType!=NodeType.WallNode and
                    not(nodeMatrix[r2][c0] in newInQueueNodes) and
                    nodeMatrix[r2][c0].nodeStatus!=NodeStatus.Explored):
                        nodeMatrix[r2][c0].previousNode = node
                        newInQueueNodes.append(nodeMatrix[r2][c0])
                if (c1>=0 and
                    nodeMatrix[r0][c1].nodeType!=NodeType.WallNode and
                    not(nodeMatrix[r0][c1] in newInQueueNodes) and
                    nodeMatrix[r0][c1].nodeStatus!=NodeStatus.Explored):
                        nodeMatrix[r0][c1].previousNode = node
                        newInQueueNodes.append(nodeMatrix[r0][c1])
                if (c2<self._sizeOfBoard and
                    nodeMatrix[r0][c2].nodeType!=NodeType.WallNode and
                    not(nodeMatrix[r0][c2] in newInQueueNodes) and
                    nodeMatrix[r0][c2].nodeStatus!=NodeStatus.Explored):
                        nodeMatrix[r0][c2].previousNode = node
                        newInQueueNodes.append(nodeMatrix[r0][c2])
            #check if end node is found
            inQueueNodes = newInQueueNodes
            for node in inQueueNodes:
                if node.nodeType == NodeType.EndNode:
                    finalNode=node
                    foundEndNode = True
                else:
                    self._myButtons[node.rowIdx][node.columnIdx].config(bg="lightBlue")

        if finalNode.nodeType == NodeType.EndNode:
            currentNode = finalNode.previousNode
            while (currentNode.nodeType!=NodeType.StartNode):
                time.sleep(0.3)
                self._myButtons[currentNode.rowIdx][currentNode.columnIdx].config(bg="green")
                currentNode = currentNode.previousNode
        return True

    def DSFAlg(self):

        inQueueNodes = []
        nodeMatrix = defaultdict(list)
        for row in range(0,self._sizeOfBoard):
            for column in range(0,self._sizeOfBoard):
                nodeType = NodeType.NormalNode
                if self._myButtons[row][column]["background"] == "orange":
                    nodeType = NodeType.StartNode
                elif self._myButtons[row][column]["background"] == "yellow":
                    nodeType = NodeType.EndNode
                elif self._myButtons[row][column]["background"] == "black":
                    nodeType = NodeType.WallNode
                node = Node(row,column,nodeType,NodeStatus.Unexplored)
                nodeMatrix[row].append(node)
                if (node.nodeType == NodeType.StartNode):
                    node.nodeStatus=NodeStatus.Explored
                    inQueueNodes.append(node)
        if len(inQueueNodes) == 0:
            return False
        foundEndNode = False
        noExplorablesLeft = False
        while(foundEndNode == False and noExplorablesLeft == False):
            time.sleep(0.3)
            idx = len(inQueueNodes)-1
            currentNode = inQueueNodes[idx]
            currentNode.nodeStatus = NodeStatus.Explored
            if(currentNode.nodeType == NodeType.StartNode):
                if(not self.HasExploreableAdjacentNodes(nodeMatrix,currentNode.rowIdx,currentNode.columnIdx)):
                    noExplorablesLeft = True
            elif(currentNode.nodeType == NodeType.EndNode):
                foundEndNode = True
            else:
                self._myButtons[currentNode.rowIdx][currentNode.columnIdx].config(bg="lightBlue")
            
            #check for new nodes
            if(self.HasExploreableAdjacentNodes(nodeMatrix,currentNode.rowIdx,currentNode.columnIdx) and currentNode.nodeType != NodeType.EndNode):
                #Left
                if(self.IsExploreableNode(nodeMatrix,currentNode.rowIdx,currentNode.columnIdx-1)):
                    node=nodeMatrix[currentNode.rowIdx][currentNode.columnIdx-1]
                    node.previousNode=currentNode
                    inQueueNodes.append(node)
                #Upper
                elif(self.IsExploreableNode(nodeMatrix,currentNode.rowIdx-1,currentNode.columnIdx)):
                    node=nodeMatrix[currentNode.rowIdx-1][currentNode.columnIdx]
                    node.previousNode=currentNode
                    inQueueNodes.append(node)
                #Right
                elif(self.IsExploreableNode(nodeMatrix,currentNode.rowIdx,currentNode.columnIdx+1)):
                    node=nodeMatrix[currentNode.rowIdx][currentNode.columnIdx+1]
                    node.previousNode=currentNode
                    inQueueNodes.append(node)
                #Lower
                elif(self.IsExploreableNode(nodeMatrix,currentNode.rowIdx+1,currentNode.columnIdx)):
                    node=nodeMatrix[currentNode.rowIdx+1][currentNode.columnIdx]
                    node.previousNode=currentNode
                    inQueueNodes.append(node)                    
            #turn back if no nodes to explore
            elif(currentNode.nodeType != NodeType.StartNode and currentNode.nodeType != NodeType.EndNode):
                self._myButtons[currentNode.rowIdx][currentNode.columnIdx].config(bg="blue")
                currentNode = currentNode.previousNode
                inQueueNodes.pop()
                while(currentNode.nodeType != NodeType.StartNode and not self.HasExploreableAdjacentNodes(nodeMatrix,currentNode.rowIdx,currentNode.columnIdx)):
                    time.sleep(0.3)
                    self._myButtons[currentNode.rowIdx][currentNode.columnIdx].config(bg="blue")
                    currentNode = currentNode.previousNode
                    inQueueNodes.pop()
        #if found EndNode:
        if(foundEndNode):
            inQueueNodes.pop(0)
            inQueueNodes.pop(len(inQueueNodes)-1)
            inQueueNodes.reverse()
            for node in inQueueNodes:
                time.sleep(0.3)
                self._myButtons[node.rowIdx][node.columnIdx].config(bg="green")
        return True

    def StartClick(self):
        if self._algNum == 0:
            threading.Thread(target=self.DijkstraAlg).start()
        elif self._algNum == 1:
            threading.Thread(target=self.DSFAlg).start()

    def ClearStartNode(self):
        for row in range(0,self._sizeOfBoard):
            for column in range(0,self._sizeOfBoard):
                if self._myButtons[row][column]["background"] == "orange":
                    self._myButtons[row][column].config(bg="white")

    def ClearEndNode(self):
        for row in range(0,self._sizeOfBoard):
            for column in range(0,self._sizeOfBoard):
                if self._myButtons[row][column]["background"] == "yellow":
                    self._myButtons[row][column].config(bg="white")

    def OnButtonClick(self,r,c):
        if self._cursorType == 0 and self._myButtons[r][c]["background"] != "yellow":
            #Start Node mode
            self.ClearStartNode()
            self._myButtons[r][c].config(bg="orange")
        elif self._cursorType == 1 and self._myButtons[r][c]["background"] != "orange":
            #End Node mode
            self.ClearEndNode()
            self._myButtons[r][c].config(bg="yellow")
        elif self._cursorType == 2 and self._myButtons[r][c]["background"] != "yellow" and self._myButtons[r][c]["background"] != "orange":
            #Wall Node mode
            self._myButtons[r][c].config(bg="black")
    
    def Test(self):
        for i in range(0,self._sizeOfBoard):
            time.sleep(1)
            self._myButtons[0][i].config(bg="blue")

    def refresh(self):
        self._root.update()
        self._root.after(1000,self.refresh)
