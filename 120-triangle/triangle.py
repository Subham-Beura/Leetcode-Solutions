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
            res= min(minTotal(r+1,i),minTotal(r+1,i+1))+triangle[r][i]
            cache[(r,i)]=res
            return res
        return minTotal(0,0)