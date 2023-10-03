class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1] * n for _ in range(m)]
        def dfs(r,c):
          if r==m-1 or c==n-1:
            return 1
          if dp[r][c] !=-1:
            return dp[r][c]
          dp[r][c]=dfs(r+1,c)+dfs(r,c+1)
          return dp[r][c]
        return dfs(0,0)