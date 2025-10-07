class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque

def cloneGraph(node : Node):
  if not node:
      return None

  oldToNew = {}
  oldToNew[node] = Node(node.val)
  q = deque([node])

  while q:
      cur = q.popleft()
      for nei in cur.neighbors:
          if nei not in oldToNew:
              oldToNew[nei] = Node(nei.val)
              q.append(nei)
          oldToNew[cur].neighbors.append(oldToNew[nei])

  return oldToNew[node]


    

          