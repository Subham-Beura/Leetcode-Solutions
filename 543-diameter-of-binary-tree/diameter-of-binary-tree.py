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
        self.maxd=0 
        def depth(root):
          if not root:
            return 0
          left=depth(root.right)
          right=depth(root.left)
          dia=left+right
          self.maxd=max(self.maxd,dia)
          return max(left,right)+1 
        depth(root)
        return self.maxd