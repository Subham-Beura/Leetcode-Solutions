class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxL=0
        L,R=0,0
        chars=set()
        for R in range(len(s)):
          while s[R] in chars:
            chars.remove(s[L])
            L+=1
          chars.add(s[R])
          maxL=max(maxL,R-L+1)
        return maxL
