# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest=[]    
        def dfs(root,parent):
            if not root:
                return
            dfs(root.left,root)
            dfs(root.right,root)
            
            if root.val not in to_delete:
                return 

            root.left and forest.append(root.left)
            root.right and forest.append(root.right)
            if parent.left==root:
                parent.left=None
            else:
                parent.right=None
        
        dfs(root,root)
        if root.val not in to_delete:
            forest.append(root)
        return forest