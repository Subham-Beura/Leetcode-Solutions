class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        maxLen=0
        for i in range(len(s)):
          l,r=i,i
          while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1) > maxLen:
              res=s[l:r+1]
              # maxLen+=2
              maxLen=r-l+1
            l-=1
            r+=1
          # Even
          l,r=i,i+1
          while l>=0 and r<len(s) and s[l]==s[r]:
            if(r-l+1) > maxLen :
              res=s[l:r+1]
              # maxLen+=2
              maxLen=r-l+1
            l-=1
            r+=1
        return res