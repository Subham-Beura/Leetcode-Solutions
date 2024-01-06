class Solution(object):
    def __init__(self):
        cache={0:1,1:1,2:2}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cache={0:1,1:1,2:2}
        return self.countBST(n)
    def countBST(self,n):
        if n in self.cache:
            return self.cache[n]
        res=0
        for i in range(1,n+1):
            res+=self.countBST(i-1)*self.countBST(n-i)
        self.cache[n]=res
        return res
        