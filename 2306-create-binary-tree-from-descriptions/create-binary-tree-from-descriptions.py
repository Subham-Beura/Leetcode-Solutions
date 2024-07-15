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
        map={}
        for n in descriptions:
            p=n[0]
            c=n[1]
            isLeft=n[2]
            if c not in map.keys():
                map[c]=TreeNode(c)
            if p not in map.keys():
                map[p]=TreeNode(p)
            allNode.add(c)
            if isLeft==1:
                map[p].left=map[c]
            else:
                map[p].right=map[c]
        for node in map.keys():
            if node not in allNode:
                return map[node]
        return None
            
