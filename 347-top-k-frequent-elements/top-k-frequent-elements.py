class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        revCounter=[(v,key)for key,v in Counter(nums).items()]
        res= heapq.nlargest(k,revCounter)
        return [key for val,key in res]
        