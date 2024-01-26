class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Set up preq graph
        preqs={i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            preqs[c].append(p)
        visited=set()

        def dfs(c):
            if c in visited:
                return False
            if preqs[c]==[]:
                return True
            
            visited.add(c)
            for p in preqs[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            preqs[c]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            