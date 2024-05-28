class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        n=len(nums)
        def findWays(i,value):
            if i==n:
                return 1 if value==target else 0
            if (i,value) in dp:
                return dp[(i,value)]
            left=findWays(i+1,value+nums[i])
            right=findWays(i+1,value-nums[i])
            dp[(i,value)]=left+right
            return dp[(i,value)]
        return findWays(0,0)