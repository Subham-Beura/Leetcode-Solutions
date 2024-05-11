# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter=-1
    def maxHeight(self,root):
        if root is None:
            return 0
        
        leftHeight=self.maxHeight(root.left)
        rightHeight=self.maxHeight(root.right)

        self.diameter=max(self.diameter,leftHeight+rightHeight+1)
        return max(leftHeight,rightHeight)+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxHeight(root)
        return self.diameter-1