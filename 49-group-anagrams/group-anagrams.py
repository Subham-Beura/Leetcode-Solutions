class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=defaultdict(list)

        for s in strs:
          count=[0]*26

          for c in s:
            i=ord(c)-ord('a')
            count[i]+=1
          res[tuple(count)].append(s)
        

        return res.values()