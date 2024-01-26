class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Set up preq graph
        preqs={i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            preqs[c].append(p)
        visited=set()
        res=[]
        def dfs(c):
            if c in visited:
                return False
            if preqs[c]==[]:
                return True
            
            visited.add(c)
            for p in preqs[c]:
                if not dfs(p):
                    return False
            res.append(c)
            visited.remove(c)
            preqs[c]=[]
            return True
        for c in range(numCourses):
            if preqs[c]==[]:
                res.append(c)
        for c in range(numCourses):
                if not dfs(c):
                    return []
        return res

        