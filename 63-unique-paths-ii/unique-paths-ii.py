class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        oG=obstacleGrid
        R=len(obstacleGrid)
        C=len(obstacleGrid[0])

        dp=[[1]*C for _ in range(R)]
        oFound=False
        for c in range(C-1,-1,-1):
            if oG[-1][c]==1:
                oFound=True
            dp[-1][c]=1 if not oFound else 0
        oFound=False    
        for r in range(R-1,-1,-1):
            if oG[r][-1]==1:
                oFound=True
            dp[r][-1]=1 if not oFound else 0
         
        for r in range(R-2,-1,-1):
            for c in range(C-2,-1,-1):
                if oG[r][c]==1:
                    dp[r][c]=0
                    continue
                dp[r][c]=dp[r+1][c]+dp[r][c+1]

        return dp[0][0] 