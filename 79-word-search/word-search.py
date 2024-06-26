class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        R=len(board) 
        C=len(board[0]) 
        def checkFrom(r,c,i,path):
            if (r,c) in path:
                return False 
            if r<0 or c<0 or r>=R or c>=C:
                return False
            if i==len(word)-1 and board[r][c]==word[-1]:
                return True
            if word[i]!=board[r][c]:
                return False
            # print(f"{r} {c} {word[i]} {board[r][c]}")
            res=False
            for v,h in directions:
               res=res or checkFrom(r+v,c+h,i+1,path+[(r,c)]) 
            return res
        res=False
        for r in range(0,R):
            for c in range(0,C):
                if checkFrom(r,c,0,[]):
                    return True
        return False