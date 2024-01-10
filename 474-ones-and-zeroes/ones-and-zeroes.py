class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        cache={}
        def find(i,m,n):
            if (i,m,n) in cache:
                return cache[(i,m,n)]
            if i==len(strs):
                return 0
            w=strs[i]
            mc=w.count("0")
            nc=w.count("1")

            if m-mc<0 or n-nc<0:
                cache[(i,m,n)]= find(i+1,m,n)
            else:
                cache[i,m,n]=max(find(i+1,m,n),find(i+1,m-mc,n-nc)+1)
            return cache[i,m,n]
        return find(0,m,n)