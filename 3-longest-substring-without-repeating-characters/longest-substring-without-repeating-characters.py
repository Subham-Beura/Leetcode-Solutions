class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        charSet=set()
        l,r=0,0
        for i in range(len(s)):
          while s[i] in charSet:
            charSet.remove(s[l])
            l+=1
          charSet.add(s[r])
          res=max(res,r-l+1) 
          r+=1
        return res