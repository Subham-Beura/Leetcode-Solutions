class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        cache=[1]*n
        LIS=-1
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    cache[i]=max(cache[i],cache[j]+1)
            LIS=max(LIS,cache[i])
            
        return LIS

            

        