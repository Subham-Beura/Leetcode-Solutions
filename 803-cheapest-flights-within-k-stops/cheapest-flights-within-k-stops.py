class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G=collections.defaultdict(list)
        for s,d,price in flights:
            G[s].append((d,price))
        queue=[(0,-1,src)]

        cheapestPrice=[float("inf")]*n

        while queue:
            current_price,stops,port=queue.pop(0)
            if stops>k:
                continue
            cheapestPrice[port]=min(cheapestPrice[port],current_price)
  
            for nei,p in G[port]:
                new_price=current_price+p
                if  stops>k or new_price > cheapestPrice[nei]:
                    continue
                queue.append((new_price,stops+1,nei))
        return cheapestPrice[dst] if cheapestPrice[dst] !=float("inf") else -1
                

