class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        n=len(coins) 
        def noOfWays(value,ci):
            if value==0:
                return 1
            if value<0 or ci==n:
                return 0
            if (value,ci) in dp:
                return dp[(value,ci)]
            res=0
            take=noOfWays(value-coins[ci],ci)
            notake=noOfWays(value,ci+1)
            res=take+notake
            dp[(value,ci)]=res
            return res
        return noOfWays(amount,0)
        