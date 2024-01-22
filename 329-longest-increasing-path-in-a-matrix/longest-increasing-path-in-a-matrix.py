class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        @cache
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n:
                return 0
            directions=[[0,1],[0,-1],[1,0],[-1,0]]
            res=0
            for d in directions:
                rs=d[0]
                cs=d[1]
                if r+rs<0 or c+cs<0 or r+rs>=m or c+cs>=n:
                    continue
                if matrix[r+rs][c+cs]>matrix[r][c]:
                    res=max(res,dfs(r+rs,c+cs)+1)
            return res
        res=0
        for r in range(m):
            for c in range(n):
                res=max(res,dfs(r,c))

        return res+1    
                



            