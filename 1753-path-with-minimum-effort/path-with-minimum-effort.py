class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R=len(heights)
        C=len(heights[0])
        visited=[[False]*C for _ in range(R)]

        minHeap=[(0,(0,0))]
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        

        while minHeap:
            max_effort,(r,c)=heapq.heappop(minHeap)

            if visited[r][c]:
                continue
            visited[r][c]=True

            if r==R-1 and c==C-1:
               return max_effort 
            
            for v,h in directions:
                new_r=r+v
                new_c=c+h
                if new_r<0 or new_r>=R or new_c<0 or new_c>=C or visited[new_r][new_c]:
                    continue
                new_effort=max(max_effort,abs(heights[r][c]-heights[new_r][new_c]))
                if new_effort>=max_effort:
                    heapq.heappush(minHeap,(new_effort,(new_r,new_c)))
        return -1