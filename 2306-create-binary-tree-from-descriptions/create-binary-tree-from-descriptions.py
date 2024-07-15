# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # map={node:parent}
        parents=[x[0] for x in descriptions]
        childs=[x[1] for x in descriptions]
        allNode=set(parents+childs)
        map={i:TreeNode(i) for i in allNode }
        for n in descriptions:
            p=n[0]
            c=n[1]
            isLeft=n[2]
            allNode.remove(c)
            if isLeft==1:
                map[p].left=map[c]
            else:
                map[p].right=map[c]
        root=allNode.pop()
        return map[root]
            
