class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        nums.sort()
        minDiff=float('inf')
        for i in range(4):
            L,R=i,len(nums)-1 -(3-i)
            diff=nums[R]-nums[L]
            minDiff=min(minDiff,diff)
        return minDiff
            