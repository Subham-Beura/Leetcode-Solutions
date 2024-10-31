class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G=collections.defaultdict(list)
        for s,d,w in times:
            G[s].append((d,w))
        
        visited=set()
        # Min Heap to store the Edges and get cheapest possible edges every time
        # Use Format (total_cost,edge_name)
        minHeap=[(0,k)]
        maxTime=0

        while minHeap:
            # Get cheapest edge to expand
            weight,node=heapq.heappop(minHeap)
            
            # Skip if already visited
            if node in visited:
                continue
            
            # Add to visited list to prevent cycles
            visited.add(node)

            # Check if dist from src to this node is max Distance. DJA gives 
            maxTime=max(maxTime,weight)

            for nei,w in G[node]:
                if nei not in visited:
                    heapq.heappush(minHeap,(weight+w,nei))
        return maxTime if len(visited)==n else -1

