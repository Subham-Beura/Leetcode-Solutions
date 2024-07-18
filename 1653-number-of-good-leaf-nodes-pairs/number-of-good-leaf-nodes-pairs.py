# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    distToLeaf={}
    count=0
    d=0
    def getDistToLeaf(self,root):
        if not root:
            return
        if not root.left and not root.right:
            self.distToLeaf[root]=[0]
            return
        self.getDistToLeaf(root.left)
        self.getDistToLeaf(root.right)
        
        leftLeafs=self.distToLeaf[root.left][::] if root.left else []
        rightLeafs=self.distToLeaf[root.right][::] if root.right else []
        
        leftLeafs=[l+1 for l in leftLeafs]
        rightLeafs=[r+1 for r in rightLeafs]

        self.distToLeaf[root]=rightLeafs+leftLeafs
        if not leftLeafs or not rightLeafs:
            return 
        # print(root.val)
        for l in leftLeafs:
            for r in rightLeafs:
                # print(f"{l} {r}")
                if l+r<=self.d:
                    
                    self.count+=1
        return 
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.distToLeaf={}
        self.d=distance
        self.getDistToLeaf(root)
        distToLeaf=self.distToLeaf
        # for k in self.distToLeaf:
        #     print(f"{k.val} : {self.distToLeaf[k]}")
        return self.count