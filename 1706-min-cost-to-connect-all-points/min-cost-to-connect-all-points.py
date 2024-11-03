class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap=[(0,0)]
        visited=[False]*(len(points))
        total=0
        while minHeap:
            edge_cost,n=heapq.heappop(minHeap)

            if visited[n]:
                continue
            visited[n]=True
            total+=edge_cost
            for i,(x,y) in enumerate(points):
                if  visited[i]:
                    continue
                cost=abs(x-points[n][0])+abs(y-points[n][1])
                heapq.heappush(minHeap,(cost,i))
        return total
