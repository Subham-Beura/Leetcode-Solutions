# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels=[]
        if not root:
            return []
        currLevel=[root]
        nextLevel=[]
        while currLevel: 
            # Push Child Node to next level
            for n in currLevel:
                if(n.left):
                    nextLevel.append(n.left)
                if(n.right):
                    nextLevel.append(n.right)

            levels.append([n.val for n in currLevel])
            currLevel=nextLevel
            nextLevel=[]
        return levels 
            