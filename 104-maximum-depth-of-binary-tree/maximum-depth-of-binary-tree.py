# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):

          if not root:
            return 0
          left,right=0,0
          if root.left:
            left=depth(root.left)
          if root.right:
            right=depth(root.right)
          return max(left,right)+1
        return depth(root)