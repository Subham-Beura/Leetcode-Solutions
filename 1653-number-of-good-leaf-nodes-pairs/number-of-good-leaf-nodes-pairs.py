# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    distToLeaf={}
    count=0
    def getDistToLeaf(self,root,d):
        if not root:
            return
        if not root.left and not root.right:
            self.distToLeaf[root]=[0]
            return
        self.getDistToLeaf(root.left,d)
        self.getDistToLeaf(root.right,d)
        
        leftLeafs=self.distToLeaf[root.left][::] if root.left else []
        rightLeafs=self.distToLeaf[root.right][::] if root.right else []
        
        leftLeafs=[l+1 for l in leftLeafs]
        rightLeafs=[r+1 for r in rightLeafs]
        self.distToLeaf[root]=rightLeafs+leftLeafs


        for l in leftLeafs:
            for r in rightLeafs:
                if l+r<=d:
                    
                    self.count+=1
        return 
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.distToLeaf={}
        self.getDistToLeaf(root,distance)

        return self.count