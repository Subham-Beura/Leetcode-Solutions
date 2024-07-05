class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            return 0 if nums[0]>nums[1] else 1 
        L,R=0,len(nums)-1
        while L<=R:
            mid=(L+R)//2
            if nums[mid-1]>nums[mid]:
                R=mid-1
            else:
                L=mid+1
        return L-1