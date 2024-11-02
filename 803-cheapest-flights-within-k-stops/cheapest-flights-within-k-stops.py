class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G=collections.defaultdict(list)
        for s,d,price in flights:
            G[s].append((d,price))
        minHeap=[(0,0,src)]

        cheapestPrice=[float("inf")]*n

        while minHeap:
            current_price,stops,port=minHeap.pop(0)
            if stops-1>k:
                continue
            cheapestPrice[port]=min(cheapestPrice[port],current_price)
  
            for nei,p in G[port]:
                new_price=current_price+p
                if  stops-1>k :
                    continue
                if new_price <= cheapestPrice[nei]:
                    minHeap.append((new_price,stops+1,nei))
        return cheapestPrice[dst] if cheapestPrice[dst] !=float("inf") else -1
                

