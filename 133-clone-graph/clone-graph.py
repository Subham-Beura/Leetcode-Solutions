"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph={None:None}
        if not node:
            return None
        if node.neighbors==[]:
            return Node(node.val)
        def dfs(node):
            if node not in graph:
                graph[node]=Node(node.val)
                for n in node.neighbors:
                    graph[node].neighbors.append(dfs(n))
            return graph[node]
        return dfs(node)