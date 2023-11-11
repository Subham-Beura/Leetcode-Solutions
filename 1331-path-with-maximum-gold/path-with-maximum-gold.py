class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited=[[False]*len(grid[0]) for _ in grid]
        def getMaxGold(r,c):
          if r<0 or c<0 or r>=len(grid) or c>= len(grid[0]):
            return 0
          if grid[r][c]==0:
            return 0
          if visited[r][c]==True:
            return 0
          visited[r][c]=True
          Gold= [getMaxGold(r,c+1),getMaxGold(r,c-1),getMaxGold(r+1,c),getMaxGold(r-1,c)]
          maxGold=max(Gold)
          visited[r][c]=False
          return maxGold+grid[r][c]
        res=[]
        for r in range(len(grid)):
          for c in range(len(grid[0])):
            if grid[r][c]!=0:
              res.append(getMaxGold(r,c))
        if res==[]:
          return 0
        return max(res)