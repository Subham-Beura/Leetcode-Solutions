class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        G=collections.defaultdict(list)

        for x1,y1 in points:
            for x2,y2 in points:
                cost=abs(x1-x2)+abs(y1-y2)
                G[(x1,y1)].append(((x2,y2),cost))
        
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
