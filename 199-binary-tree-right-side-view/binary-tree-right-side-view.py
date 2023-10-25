# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
          return []
        res=[]
        lot,level=[],[root]
        while level:
          lot.append([node.val for node in level])
          res.append(level[-1].val)
          temp=[]
          for node in level:
            temp.extend([node.left,node.right])
          level=[child for child in temp if child]
        return res 
        