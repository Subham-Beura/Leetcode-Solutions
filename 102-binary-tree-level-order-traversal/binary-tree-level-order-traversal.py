# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
          return []
        ans,level=[],[root]
        while level:
          # Add this level to answer
          ans.append([a.val for a in level])
          # Add childrens of this level
          nextLevel=[]
          for a in level:
            nextLevel.extend([a.left,a.right])
          level=[child for child in nextLevel if child]
        return ans

        