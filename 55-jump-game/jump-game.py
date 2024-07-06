class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxRange=0
        for i,n in enumerate(nums):
            if i>maxRange:
                return False
            maxRange=max(maxRange,n+i)
        print(maxRange)
        return maxRange>=len(nums)-1