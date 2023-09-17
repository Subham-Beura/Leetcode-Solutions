class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*n
        def noOfWays(i):
          if i==n:
            return 1
          if i>n:
            return 0
          if dp[i]!=-1:
            return dp[i]
          dp[i]= noOfWays(i+1)+noOfWays(i+2)
          return dp[i]
        return noOfWays(0)        