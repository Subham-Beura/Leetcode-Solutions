class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        tower=[[0]*(i+1) for i in range(query_row+2) ]
        # Pouring
        tower[0][0]=poured
        for i in range(query_row+1):
            for j in range(i+1):
                if i==query_row and j==query_glass:
                    return min(tower[i][j],1.0) 
                if tower[i][j]<=1:
                    continue
                overflow=float(tower[i][j]-1)
                tower[i+1][j]+=overflow/2
                tower[i+1][j+1]+=overflow/2
                tower[i][j]=1
        return tower[query_row][query_glass]