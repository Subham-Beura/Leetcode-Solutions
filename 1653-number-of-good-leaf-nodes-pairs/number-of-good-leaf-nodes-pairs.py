# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    distToLeaf={}
    def getDistToLeaf(self,root):
        if not root:
            return
        if not root.left and not root.right:
            self.distToLeaf[root]=[0]
            return
        self.getDistToLeaf(root.left)
        self.getDistToLeaf(root.right)
        leftLeafs=[]
        rightLeafs=[]
        if root.left:
            leftLeafs=self.distToLeaf[root.left][::]
        if root.right:
            rightLeafs=self.distToLeaf[root.right][::]
        
        self.distToLeaf[root]=[]
        for i,l in enumerate(leftLeafs):
            leftLeafs[i]+=1

        for i,l in enumerate(rightLeafs):
            rightLeafs[i]+=1
        self.distToLeaf[root]=rightLeafs+leftLeafs
        return 
    count=0
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.distToLeaf={}
        self.getDistToLeaf(root)
        distToLeaf=self.distToLeaf
        # for k in self.distToLeaf:
        #     print(f"{k.val} : {self.distToLeaf[k]}")
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            leftLeafs=distToLeaf[root.left] if root.left else []
            rightLeafs=distToLeaf[root.right] if root.right else []
            if not leftLeafs or not rightLeafs:
                return
            # print(root.val)
            for l in leftLeafs:
                for r in rightLeafs:
                    if l+r+2<=distance:
                        # print(f"{l} {r} ")
                        self.count+=1
        dfs(root)
        return self.count