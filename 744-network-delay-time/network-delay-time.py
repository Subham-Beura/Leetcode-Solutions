class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G=collections.defaultdict(list)
        for s,d,w in times:
            G[s].append((d,w))
        
        visited=set()

        minHeap=[(0,k)]
        res=0
        while minHeap:
            cost_to_reach,v=heapq.heappop(minHeap)
            
            if v in visited:
                continue
            visited.add(v)


            res=max(res,cost_to_reach)

            for nei,w in G[v]:
                if nei not in visited:
                    heapq.heappush(minHeap,(cost_to_reach+w,nei))
        return res if len(visited)==n else -1
