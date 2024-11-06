class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        @cache
        def profit(day,hasBought):
            if day>=n:
                return 0
            if hasBought:
                return max(profit(day+1,False)+prices[day]-fee,profit(day+1,True))
            return max(profit(day+1,True)-prices[day],profit(day+1,False))
        return profit(0,False)