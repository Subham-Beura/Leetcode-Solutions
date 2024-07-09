class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        map=Counter(nums)
        for i,color in enumerate(nums):
            if i<map[0]:
                nums[i]=0
            elif i<map[0]+map[1] :
                nums[i]=1
            else:
                nums[i]=2
        
        