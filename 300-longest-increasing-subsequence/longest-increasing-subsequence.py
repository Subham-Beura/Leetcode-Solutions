class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengthOfLIS=[1]*(len(nums))
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[j]< nums[i]:
                    lengthOfLIS[i]=max(lengthOfLIS[i],lengthOfLIS[j]+1)
        return max(lengthOfLIS)