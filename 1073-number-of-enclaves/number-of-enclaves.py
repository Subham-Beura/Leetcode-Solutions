class Solution:
    def flagCanGetOutSideCell(self,r,c,grid):
        h,w=len(grid),len(grid[0])
        print(r)
        print(c)
        if r<0 or c<0 or r>=h or c>=w or grid[r][c] in [0,-1]:
            return
        grid[r][c]=-1
        ti=self.flagCanGetOutSideCell(r+1,c,grid) 
        bi=self.flagCanGetOutSideCell(r-1,c,grid) 
        ri=self.flagCanGetOutSideCell(r,c+1,grid) 
        li=self.flagCanGetOutSideCell(r,c-1,grid) 
    def numEnclaves(self, grid: List[List[int]]) -> int:
        h,w=len(grid),len(grid[0])
        
        for r in [0,h-1]:
            for c in range(w):
                if grid[r][c]==1:
                    self.flagCanGetOutSideCell(r,c,grid)
        for r in range(h):
            for c in [0,w-1]:
                if grid[r][c]==1:
                    self.flagCanGetOutSideCell(r,c,grid)
        res=0
        for r in range(h):
            for c in range(w):
                if grid[r][c]==1:
                    res+=1
        return res