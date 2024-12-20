class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        G=collections.defaultdict(list)
        for i,(v1,v2) in enumerate(edges):
            G[v1].append((v2,succProb[i]))
            G[v2].append((v1,succProb[i]))
        maxHeap=[(-1.0,start_node)]
        prob=[0.0]*n
        visited=[False]*n

        while maxHeap:
            cost_to_reach,node=heapq.heappop(maxHeap)
            cost_to_reach*=-1.0

            if visited[node]:
                continue
            visited[node]=True

            # prob[node]=max(prob[node],cost_to_reach)
            if node==end_node:
                return cost_to_reach
            for nei,p in G[node]:
                new_prob=cost_to_reach*p*-1.0
                if not visited[nei] and new_prob*-1 >prob[nei] :
                    heapq.heappush(maxHeap,(new_prob,nei))
        # print(prob)
        return prob[end_node]
