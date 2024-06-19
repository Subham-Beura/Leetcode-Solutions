class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==0:
            return True
        def is_square(i: int) -> bool:
            return i == math.isqrt(i) ** 2
        # dp=[False]*(c+2)
        # for i in range(int(sqrt(c+1))+1):
        #     dp[i**2]=True
        for i in range(1,int(sqrt(c+1))+1): 
            if c-i**2>=0 and is_square(c-i**2):
                return True
            
        return False
        