class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengthOfLIS=[1]*(len(nums))
        maxLIS=0
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[j]< nums[i] and lengthOfLIS[i]<lengthOfLIS[j]+1:
                    lengthOfLIS[i]=lengthOfLIS[j]+1
                maxLIS=max(maxLIS,lengthOfLIS[i])
        return max(lengthOfLIS)