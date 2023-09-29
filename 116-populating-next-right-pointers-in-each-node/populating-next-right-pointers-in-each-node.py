"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def joinLevel(thisLevel):
          for i in range(len(thisLevel)):
            if i==len(thisLevel)-1:
              thisLevel[i].next=None
              return
            thisLevel[i].next=thisLevel[i+1]
        def bfs(root):
          if not root:
            return None
          thislevel=[root]
          while thislevel:
            nextlevel=[]
            for node in thislevel:
              if node.left:
                nextlevel.append(node.left) 
              if node.right:
                nextlevel.append(node.right)
            thislevelval=[node.val for node in thislevel]
            print(thislevelval)
            joinLevel(thislevel)
            thislevel=nextlevel
          return root
        return bfs(root)
        # return None
        