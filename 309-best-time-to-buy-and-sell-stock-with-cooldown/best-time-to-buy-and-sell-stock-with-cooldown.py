class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def profit(day,hasStock):
            if day >=n :
                return 0
            if hasStock:
                return max(profit(day+2,False)+prices[day],profit(day+1,True))
            return max(profit(day+1,True)-prices[day],profit(day+1,False))
        return profit(0,False)