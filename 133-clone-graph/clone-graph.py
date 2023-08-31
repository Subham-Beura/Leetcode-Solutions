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
        oldToNew={}

        if not node:
          return node
        def clone(node):
          if node in oldToNew:
            return oldToNew[node]
          copy=Node(node.val)
          oldToNew[node]=copy

          for nei in node.neighbors:
            copy.neighbors.append(clone(nei))
          return copy

        return clone(node)