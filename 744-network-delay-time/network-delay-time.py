class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G=collections.defaultdict(list)
        for s,d,w in times:
            G[s].append((d,w))
        
        visited=set()
        minHeap=[(0,k)]
        maxTime=0

        while minHeap:
            weight,node=heapq.heappop(minHeap)
            
            if node in visited:
                continue
            visited.add(node)

            maxTime=max(maxTime,weight)

            for nei,w in G[node]:
                if nei not in visited:
                    heapq.heappush(minHeap,(weight+w,nei))
        return maxTime if len(visited)==n else -1

