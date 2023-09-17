"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        newNode=None
        oldToNew={} 
        def dfs(node):
          if node in oldToNew:
            return oldToNew[node]
          copy=Node(node.val)
          oldToNew[node]=copy
          for n in node.neighbors:
            copy.neighbors.append(dfs(n))
          return copy

        if node is None:
          return node
        newNode=dfs(node) 
        print(newNode)
        return newNode