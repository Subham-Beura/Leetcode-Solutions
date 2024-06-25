class Solution:
    n=0
    def isHappy(self, n: int) -> bool:
        def getSumOfSquares(n):
            sumOfSquare=0
            resv=n
            while(n):
                lastD=n%10
                sumOfSquare+=lastD**2
                n=n//10
            return sumOfSquare 
        path=set()
        def helper(n):
            if n in path:
                return False
            sumOfSquare=getSumOfSquares(n) 
            if sumOfSquare==1:
                return True
            path.add(n)
            return helper(sumOfSquare)
        self.n=0
        if n in (1,7):
            return True
        return helper(n)
        