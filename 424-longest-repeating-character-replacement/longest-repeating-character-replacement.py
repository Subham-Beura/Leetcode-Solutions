class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count={}
        res=0

        L=0
        maxf=0
        for R in range(len(s)):
          count[s[R]]=1+count.get(s[R],0)
          maxf=max(maxf,count[s[R]])
          while (R+1-L)-maxf>k:
            count[s[L]]-=1
            L+=1
          
          res=max(res,R+1-L)
        
        return res



