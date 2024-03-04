class Solution:
    def mySqrt(self, x: int) -> int:
        L,R=0,x
        while L<=R:
            mid=(L+R)//2
            print(f'{L} {mid} {R}')
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                R=mid-1
            else:
                L=mid+1
        return R