class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        m,n=len(mat),len(mat[0])
        res=[[-1]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if mat[r][c]==0:
                    q.append((r,c))
                    res[r][c]=0
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        dist=0
        while q:
            dist=dist+1
            for _ in range(len(q)):
                r,c=q.popleft()
                # print(f"----{r} {c} {dist}")
                for v,h in dirs:
                    nr,nc=v+r,c+h
                    # print(f"{nr} {nc} {dist}")
                    if nr<m and nc<n and nr>=0 and nc>=0 and res[nr][nc]==-1 and mat[nr][nc]==1 :
                        # print(f"..{nr} {nc} {dist}")
                        q.append((nr,nc))
                        res[nr][nc]=dist
        return res