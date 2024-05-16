class Solution:
    path=set()
    # def borderFound(self,r,c,board):
    #     h,w=len(board),len(board[0])
    #     if board[r][c]=="X":
    #         return False
    #     if (r in [0,h-1] or c in [0, w-1]):
    #         return True
    #     if (r,c) in self.path:
    #         return False
    #     self.path.append((r,c))
    #     t=self.borderFound(r+1,c,board)
    #     b=self.borderFound(r-1,c,board)
    #     ri=self.borderFound(r,c+1,board)
    #     le=self.borderFound(r,c-1,board)    
    #     return t or b or ri or le
    def fill(self,r,c,board):
        h,w=len(board),len(board[0])
        if r<0 or c<0 or r>=h or c>=w:
            return 
        if board[r][c]=="X":
            return 
        if (r,c) in self.path:
            return False
        board[r][c]="S"
        self.path.append((r,c))
        t=self.fill(r+1,c,board)
        b=self.fill(r-1,c,board)
        ri=self.fill(r,c+1,board)
        le=self.fill(r,c-1,board)    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h,w=len(board),len(board[0])
        for r in range(h):
            for c in range(w):
                if board[r][c]=="O":
                    self.path=[]
                    if (r in [0,h-1] or c in [0, w-1]):
                        self.fill(r,c,board)
        for r in range(h):
            for c in range(w):
                if board[r][c]!="S":
                    board[r][c]="X"
                    continue
                board[r][c]="O"