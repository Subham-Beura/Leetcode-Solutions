class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        res = []
        prev = self.permute(nums[:-1])
        for p in prev:
            for i in range(len(p) + 1):
                newP = p[:i] + [nums[-1]] + p[i:]
                res.append(newP)
        return res
