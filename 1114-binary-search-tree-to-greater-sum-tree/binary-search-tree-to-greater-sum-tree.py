# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    inord=[]
    c=0
    def inorder(self,root):
        if not root:
            return 
        self.inorder(root.right)
        self.c+=root.val
        root.val=self.c
        self.inorder(root.left)
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.inorder(root)
        return root
        