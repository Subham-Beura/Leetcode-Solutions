class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            return 0 if nums[0]>nums[1] else 1 
        L,R=0,len(nums)-1
        while L<=R:
            mid=(L+R)//2
            if (mid==0 and nums[1]<nums[0]) or (mid==len(nums)-1 and nums[-2]<nums[-1]):
                return mid
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]>nums[mid]:
                R=mid-1
            else:
                L=mid+1
        return -1