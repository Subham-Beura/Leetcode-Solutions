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
        isValid=True
        def inOrder(root):
          if root==None:
            return True
          left=inOrder(root.left)
          mid=True
          if len(res)>0 and root.val <= res[-1]:
            print(res[-1])
            mid= False
          res.append(root.val)
          right=inOrder(root.right)
          return left and mid and right
        return inOrder(root)