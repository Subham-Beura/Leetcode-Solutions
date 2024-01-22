class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=0
        def dfs(i,j):
            # Out of bounds
            if i<0 or j<0 or i>=m or j>=n:
                return  
            if grid[i][j]=="0":
                return
            grid[i][j]="0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        for r in range(m):
            for c in range(n):
                if grid[r][c]=="1":
                    dfs(r,c)
                    res+=1
        return res


        

