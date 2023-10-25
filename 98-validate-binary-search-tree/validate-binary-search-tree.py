# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res=[]
        def inOrder(root):
          if root==None:
            return 
          inOrder(root.left)
          res.append(root.val)
          inOrder(root.right)
        inOrder(root)
        print(res)
        for i in range(1,len(res)):
          if res[i]<=res[i-1]:
            return False
        return True