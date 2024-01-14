class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        cache={}
        def minTotal(r,i):
            if (r,i) in cache:
                return cache[(r,i)]
            if r==len(triangle):                
                return 0
            cache[(r,i)]= min(minTotal(r+1,i),minTotal(r+1,i+1))+triangle[r][i]
            return cache[(r,i)]
        return minTotal(0,0)