# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    inord=[]
    def inorder(self,root):
        if not root:
            return 
        self.inorder(root.left)
        self.inord.append(root.val)
        self.inorder(root.right)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.inord=[]
        self.inorder(root)
        gt=self.inord
        map=Counter(self.inord)
        add=gt[-1]
        map[add]=add
        for i in range(len(gt)-2,-1,-1):
            res=gt[i]+add 
            map[gt[i]]=res
            add=res

        def dfs(root):
            if not root:
                return
            root.val=map[root.val]
            dfs(root.left)
            dfs(root.right)
            return root
        
        return dfs(root)
        