class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        
        def noOfWays(value,minCoin):
            if value==0 or value==minCoin:
                return 1
            if value<0 or value<minCoin:
                return 0
            if (value,minCoin) in dp:
                return dp[(value,minCoin)]
            res=0
            for c in coins:
                if c<minCoin:
                    continue
                res+=noOfWays(value-c,c)
            dp[(value,minCoin)]=res
            return res
        return noOfWays(amount,0)
        