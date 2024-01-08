class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        cache={0:0}
        lastPower=1
        for i in range(1,n+1):
            if i==lastPower*2:
                lastPower=i
                cache[i]=1
                continue
            cache[i]=1+cache[i-lastPower]
        return list(cache.values())
