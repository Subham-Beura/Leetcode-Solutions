# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        
        self.flattenHelper(root)
        return root
    def flattenHelper(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if  root.left is None and  root.right is None:
            return [root,root]
        if root.left and not root.right:
            left=self.flattenHelper(root.left)
            root.right=left[0]
            root.left=None
            return [root,left[1]]
        if not root.left and root.right:
            return [root,self.flattenHelper(root.right)[1]]
        left=self.flattenHelper(root.left)
        right=self.flattenHelper(root.right)

        root.right=left[0]
        left[1].right=right[0]
        root.left=None
        return [root,right[1]] 
        