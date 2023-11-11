class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def removeLand(r,c):
          if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):
            return 
          if grid[r][c]=="0":
            return 
          grid[r][c]="0"

          removeLand(r+1,c) #Up
          removeLand(r-1,c) #Down
          removeLand(r,c+1) #Right
          removeLand(r,c-1) #Lefrt


        islandCount=0
        for r in range(len(grid)):
          for c in range(len(grid[0])):
            if grid[r][c]=="1":
              islandCount+=1
              removeLand(r,c)

        return islandCount