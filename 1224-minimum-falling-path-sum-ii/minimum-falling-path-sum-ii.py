class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # matrix=grid
        R=len(matrix)
        C=len(matrix[0])
        for i in range(R-2,-1,-1):
            print(matrix[i])
            nextRow=matrix[i+1]
            for j in range(C):
                minv=99999999
                for c,v in enumerate(nextRow):
                    if c==j:
                        continue
                    minv=min(minv,v)
                matrix[i][j]+=minv
                    
        print(matrix)
        return min(matrix[0])