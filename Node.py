import enum

class NodeType(enum.Enum):
   StartNode = 0
   EndNode = 1
   WallNode = 2
   NormalNode = 3

class NodeStatus(enum.Enum):
   Unexplored = 0
   InQueue = 1
   Explored = 2

class Node: 
    def __init__(self, rowIdx, columnIdx, nodeType = NodeType.NormalNode, nodeStatus = NodeStatus.Unexplored): 
        self._rowIdx = rowIdx
        self._columnIdx = columnIdx
        self._nodeType = nodeType
        self._nodeStatus = nodeStatus
        self._previousNode = None

    @property
    def rowIdx(self): 
        return self._rowIdx

    @property
    def columnIdx(self): 
        return self._columnIdx

    @property
    def nodeType(self): 
        return self._nodeType

    @nodeType.setter 
    def nodeType(self, a): 
        self._nodeType = a 

    @property
    def nodeStatus(self): 
        return self._nodeStatus

    @nodeStatus.setter 
    def nodeStatus(self, a): 
        self._nodeStatus = a 

    @property
    def previousNode(self): 
        return self._previousNode

    @previousNode.setter 
    def previousNode(self, a): 
        self._previousNode = a

    def __eq__(self,other):
        if self._rowIdx == other._rowIdx and self._columnIdx == other._columnIdx and self._nodeType == other._nodeType and self._nodeStatus == other._nodeStatus :
            return True
        else:
            return False


