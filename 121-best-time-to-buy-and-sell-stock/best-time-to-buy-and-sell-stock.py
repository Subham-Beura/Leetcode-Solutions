class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit=0
        lowestPrice=prices[0]
        L=0
        for R in range(len(prices)):
          profit=prices[R]-prices[L]
          if profit>0:
            maxProfit=max(maxProfit,profit)  
          if prices[R]<lowestPrice:
            L=R
            lowestPrice=prices[R]
        return maxProfit          
