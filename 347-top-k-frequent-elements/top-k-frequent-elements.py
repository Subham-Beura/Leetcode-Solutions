class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        revCounter=[(v,key)for key,v in Counter(nums).items()]
        heapq.heapify(revCounter)
        
        res= heapq.nlargest(k,revCounter)
        return [key for val,key in res]
        # if len(revCounter)==1:
        #   return [revCounter[0][1]]
        # print(revCounter)
        # if k==1:
        #   return [revCounter[-1][1]]
        # for v,key in revCounter:
        #   res.append(key)
        # print(res)
        # if k >= len(res):
        #   return res
        # return res[-k:]
        