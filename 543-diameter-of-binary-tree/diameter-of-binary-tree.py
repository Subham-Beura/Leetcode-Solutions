# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
          if not root:
            return 0
          left=depth(root.right)
          right=depth(root.left)
          return max(left,right)+1 
        global maxd
        maxd=0 
        def dfs(root):
          if not root:
            return
          dia=depth(root.right)+depth(root.left)
          global maxd
          maxd=max(maxd,dia)
          dfs(root.right)
          dfs(root.left)
        dfs(root)
        return maxd