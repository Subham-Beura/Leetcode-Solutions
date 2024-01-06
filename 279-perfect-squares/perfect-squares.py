class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache={0:0,1:1}
        for i in range(1,n+1):
            minv=i
            j=1
            while j*j <=i:
                minv=min(minv,cache[i-j*j]+1)
                j+=1
            cache[i]=minv
        return cache[n] 
