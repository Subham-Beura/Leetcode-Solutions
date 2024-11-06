class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def profit(day,hasStock,i):
            if day >=n or i>=2:
                return 0
            if hasStock:
                return max(profit(day+1,False,i+1)+prices[day],profit(day+1,True,i))
            return max(profit(day+1,True,i)-prices[day],profit(day+1,False,i))
        return profit(0,False,0)

        