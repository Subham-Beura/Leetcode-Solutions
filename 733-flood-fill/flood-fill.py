class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        sourceColor=image[sr][sc]
        if sourceColor==color:
            return image
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n:
                return
            if image[r][c]!=sourceColor:
                return    
            image[r][c]=color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(sr,sc)
        return image
               
    
    