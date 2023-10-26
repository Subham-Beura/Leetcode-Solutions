# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        LCA=None
        def dfs(root):
          if root in (None,p,q):
            return root
          left=dfs(root.left)
          right=dfs(root.right)
          return root if left and right else left or right
        return dfs(root)