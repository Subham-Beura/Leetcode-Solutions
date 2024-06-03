class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L,R=0,len(nums)-1
        res=[-1,-1]
        while L<=R:
            M=(L+R)//2
            if nums[M]==target and (M==0 or nums[M-1]!=target):
                res[0]=M 
                break
            if nums[M]>=target:
                R=M-1
            else:
                L=M+1

        L,R=0,len(nums)-1
        while L<=R:
            M=(L+R)//2
            if nums[M]==target and (M==len(nums)-1 or nums[M+1]!=target):
                res[1]=M
                break
            if nums[M]>target:
                R=M-1
            else:
                L=M+1
        return res
        