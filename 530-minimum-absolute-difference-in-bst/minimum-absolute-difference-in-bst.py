# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        inorder=[]
        def dfs(root):
          if not root:
            return []
          left=dfs(root.left)
          right=dfs(root.right)
          return left+[root.val]+right
        inorder=dfs(root)
        print(inorder)
        minVal=999999999
        for i in range(1,len(inorder)):
          if  inorder[i]==None or  inorder[i-1]==None:
            continue
          minVal=min(minVal,inorder[i]-inorder[i-1])
          print(minVal)
        return minVal