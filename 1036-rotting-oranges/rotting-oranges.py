class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOrange=0
        rottenOrange=0
        ro=deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    freshOrange+=1
                elif grid[r][c]==2:
                    rottenOrange+=1
                    ro.append((r,c))
        total=freshOrange+rottenOrange
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        count=0
        while(ro and freshOrange>0):
            count+=1
            for _ in range(len(ro)):
                r,c=ro.popleft()
                for t,d in dirs:
                    if r+t<len(grid) and r+t>=0 and c+d<len(grid[0]) and c+d>=0 and grid[r+t][c+d]==1:
                        freshOrange-=1
                        grid[r+t][c+d]=2
                        ro.append((r+t,c+d))
        return count if freshOrange==0 else -1