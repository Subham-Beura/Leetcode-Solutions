class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        R=len(matrix)
        C=len(matrix[0])
        for i in range(R-2,-1,-1):
            for j in range(C):
                if j==0:
                    matrix[i][j]+=min(matrix[i+1][0],matrix[i+1][1])
                elif j==C-1:
                    matrix[i][j]+=min(matrix[i+1][j-1],matrix[i+1][j])
                else:
                    matrix[i][j]+=min(matrix[i+1][j-1],matrix[i+1][j],matrix[i+1][j+1])
        return min(matrix[0])