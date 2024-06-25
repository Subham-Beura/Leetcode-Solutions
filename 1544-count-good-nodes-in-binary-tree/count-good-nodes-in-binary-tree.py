# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxTY):
            if not root:
                return 0
            l=dfs(root.left,max(root.val,max(root.val,maxTY)))
            r=dfs(root.right,max(root.val,max(root.val,maxTY)))
            return l+r+(1 if root.val>=maxTY else 0)
        return dfs(root,root.val) 
