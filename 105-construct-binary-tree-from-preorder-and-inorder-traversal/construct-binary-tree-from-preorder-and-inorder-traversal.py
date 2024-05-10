# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        src=TreeNode(inorder[0])
        def solve(preorder,inorder):
            if not preorder and not inorder:
                return None
            if len(preorder)==1 and len(inorder)==1:
                return TreeNode(preorder[0])
            root=TreeNode(preorder[0])
            rootIndex=inorder.index(preorder[0])
            leftPart=solve(preorder[1:rootIndex+1],inorder[:rootIndex])
            rightPart=solve(preorder[rootIndex+1:],inorder[rootIndex+1:])
            root.left=leftPart
            root.right=rightPart
            return root
        return solve(preorder,inorder)