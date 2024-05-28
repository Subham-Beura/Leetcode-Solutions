class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        @cache
        def noOfWays(value,minCoin):
            if value==0 or value==minCoin:
                return 1
            if value<0 or value<minCoin:
                return 0
            res=0
            for c in coins:
                if c<minCoin:
                    continue
                res+=noOfWays(value-c,c)
            return res
        return noOfWays(amount,0)
        