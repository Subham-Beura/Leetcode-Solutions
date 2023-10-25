# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def treeBuilder(nums):
          if nums==[]:
            return None 
          if len(nums)==1:
            return TreeNode(nums[0])
          mid=len(nums)//2
          print(mid)
          root=TreeNode(nums[mid])
          root.left=treeBuilder(nums[:mid])
          root.right=treeBuilder(nums[mid+1:])
          return root

          
        return treeBuilder(nums)