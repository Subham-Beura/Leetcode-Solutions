# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    inorderT=[]
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        self.inorderT.append(root.val)
        self.inorder(root.right)
    def buildBalancedTree(self,inorderT):
        if inorderT==[]:
            return None
        if len(inorderT)==1:
            return TreeNode(inorderT[0])
        mid=len(inorderT)//2
        newRoot=TreeNode(inorderT[mid])
        newRoot.left=self.buildBalancedTree(inorderT[:mid])
        newRoot.right=self.buildBalancedTree(inorderT[mid+1:])
        return newRoot
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorderT=[]
        self.inorder(root)
        print(self.inorderT)
        return self.buildBalancedTree(self.inorderT)