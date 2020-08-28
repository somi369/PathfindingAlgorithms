from Node import *

n = Node(1,2,NodeType.NormalNode,NodeStatus.Unexplored)

print(n.rowIdx)
print(n.columnIdx)
print(n.nodeType)
print(n.nodeStatus)
print(n.previousNode)

k = Node(5,6,NodeType.NormalNode,NodeStatus.Unexplored)

n.previousNode = k
print(n.previousNode.rowIdx)
