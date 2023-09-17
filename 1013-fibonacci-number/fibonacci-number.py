class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*(n+1)
        def findFib(i):
          if i==0 or i==1:
            return i
            
          if dp[i]!= -1:
            return dp[i]
          dp[i]=findFib(i-1)+findFib(i-2)
          return dp[i]
        return findFib(n)
        