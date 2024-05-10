class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        if amount in coins:
            return 1
        dp=[1000000000]*(amount+1) 
        for c in coins:
            if c<amount:
                dp[c]=1
        for i in range(1,amount+1):
            if dp[i]==1:
                continue
            for c in coins:
                if i-c>=0:
                    dp[i]=min(dp[i],dp[i-c]+1)
            
        return dp[amount] if dp[amount]!=1000000000 else -1

    