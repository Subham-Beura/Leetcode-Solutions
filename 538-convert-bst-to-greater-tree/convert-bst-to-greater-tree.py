# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    c=0
    def reverseInorder(self,root):
        if not root:
            return
        self.reverseInorder(root.right)
        self.c+=root.val
        root.val=self.c
        self.reverseInorder(root.left)
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverseInorder(root)
        return root
        