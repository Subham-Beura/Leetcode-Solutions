class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        cache={}
        def noPaths(coord,p):
            r,c=coord[0],coord[1]
            if r<0 or r>=m or c<0 or c>=n:
                return 1
            if p==0:
                return 0
            if (coord,p) in cache:
                return cache[(coord,p)]

            top=noPaths((r+1,c),p-1)
            bottom=noPaths((r-1,c),p-1)
            left=noPaths((r,c-1),p-1)
            right=noPaths((r,c+1),p-1)
            res=top+bottom+left+right
            cache[(coord,p)]=res
            return res
        return (noPaths((startRow,startColumn),maxMove))%(10**9+7)

        