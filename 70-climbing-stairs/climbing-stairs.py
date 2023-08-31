class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3: return n
        ways=[-1]*(n+1)
        ways[0]=0
        ways[1]=1
        ways[2]=2
        for i in range(3,n+1):
          ways[i]=ways[i-1]+ways[i-2]
        return ways[n]
                  