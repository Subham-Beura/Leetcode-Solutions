class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def findArea(r,c):
          if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
            return 0
          if grid[r][c]==0:
            return 0
          grid[r][c]=0
          area=0
          area+=findArea(r+1,c)
          area+=findArea(r-1,c)
          area+=findArea(r,c+1)
          area+=findArea(r,c-1)
          return area+1
        maxArea=0
        for r in range(len(grid)):
          for c in range(len(grid[0])):
            if grid[r][c]==1:
              # print(findArea(r,c))
              maxArea=max(maxArea,findArea(r,c))
        return maxArea
        