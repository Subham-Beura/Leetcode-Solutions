# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    LCA=None
    def getLCA(self,root,s,d):
        res=0
        if not root:
            return 0
        if root.val==s:
            res+= 1
        if root.val==d:
            res+= 2
        res+=self.getLCA(root.left,s,d)
        res+=self.getLCA(root.right,s,d)
        if not self.LCA and res==3:
            self.LCA=root
        return res
    def depthOfs(self,root,s):
        if not root:
            return 0
        if root.val==s:
            return 1
        l=self.depthOfs(root.left,s)
        r=self.depthOfs(root.right,s)
        if l!=0 or r!=0:
            return max(l,r)+1
        return 0
    def pathTod(self,root,d):
        if not root:
            return [False,""]
        if root.val==d:
            return [True,""]
        l=self.pathTod(root.left,d)
        r=self.pathTod(root.right,d)
        if l[0]:
            return [True,'L'+l[1]]
        if r[0]:
            return [True,'R'+r[1]]
        return [False,""]
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.getLCA(root,startValue,destValue)
        root=self.LCA
        # print(root.val)
        distToS=self.depthOfs(root,startValue)-1
        path='U'*(distToS)
        path+=self.pathTod(root,destValue)[1]
        # print(path)
        return path