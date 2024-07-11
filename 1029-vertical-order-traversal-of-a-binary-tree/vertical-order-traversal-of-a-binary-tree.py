# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cols={}
    # colWidth=[0,0]
    def setRowColumns(self,root,row,col):
        if not root:
            return

        if not self.cols.get(col):
            self.cols[col]=[(root.val,row)]
        else:
            self.cols[col].append((root.val,row))

        self.setRowColumns(root.left,row+1,col-1)
        self.setRowColumns(root.right,row+1,col+1)


    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.cols={}
        self.setRowColumns(root,0,0)
        cols=self.cols
        keys=list(cols.keys())
        res=[]
        for i in range(min(keys),max(keys)+1):
            nodes=cols[i]
            if not nodes:
                continue
            values=[node[0] for node in nodes]
            rows=[node[1] for node in nodes]
            if len(set(rows))==1:
                res.append(values)
                continue
            map={r:[] for r in rows }
            for n in nodes:
                map[n[1]].append(n[0])
            thisLevel=[]
            for k in sorted(map.keys()):
                map[k].sort()
                thisLevel+=map[k]
            res.append(thisLevel)
        return res