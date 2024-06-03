class Solution:
    def findMin(self, nums: List[int]) -> int:
        L,R=0,len(nums)-1
        while L<=R:
            M=(L+R)//2
            print(f"{L} {M} {R}")
            l=nums[L] 
            r=nums[R]
            m=nums[M]

            if l<=r:
                return nums[L]
            
            if M!=0 and nums[M-1]>m: 
                return nums[M] 
            if m<=r:
                R=M-1
            else:
                L=M+1
        return -1