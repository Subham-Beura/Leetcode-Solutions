class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[-1]*(amount+1)
        def findMinCoins(coins,a):
          if a==0: return 1
          if a<0: return -1
          if dp[a]!= -1:
            return dp[a]
          minCoins=9999999
          for c in coins:
            newMinCoins=findMinCoins(coins,a-c)
            if newMinCoins==-1:
              continue
            minCoins=min(minCoins,newMinCoins+1)
          dp[a]=minCoins
          return minCoins

        res= findMinCoins(coins,amount)-1
        return res if res!=9999998 else -1