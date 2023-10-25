# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(L,R):
          if not L and not R:
            return True
          if L and R and L.val==R.val:
            return isMirror(L.left,R.right) and isMirror(L.right,R.left)
          return False
        return isMirror(root,root)