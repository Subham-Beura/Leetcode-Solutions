# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # map={node:parent}

        allNode=set()
        vToNode={}
        for n in descriptions:
            p=n[0]
            c=n[1]
            isLeft=n[2]
            if c not in vToNode:
                vToNode[c]=TreeNode(c)
            if p not in vToNode:
                vToNode[p]=TreeNode(p)
            allNode.add(c)
            if isLeft==1:
                vToNode[p].left=vToNode[c]
            else:
                vToNode[p].right=vToNode[c]
        for node in vToNode.keys():
            if node not in allNode:
                return vToNode[node]
        return None
            
