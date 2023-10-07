class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)<len(p):
          return []
        L=0
        res=[]
        pSum=0
        pCounter={c:0 for c in s}
        for c in p:
          pSum+=ord(c)
          pCounter[c]=1+pCounter.get(c,0)
        windowSum=0
        windowCounter={c:0 for c in s}
        for c in range(len(p)-1):
          windowSum+=ord(s[c])
          windowCounter[s[c]]=1+windowCounter.get(s[c],0)
        for R in range(len(p)-1,len(s)):
          windowSum+=ord(s[R])
          windowCounter[s[R]]=1+windowCounter.get(s[R],0)
          if pSum==windowSum :
            if windowCounter==pCounter:
              res.append(L)
          windowSum-=ord(s[L])
          windowCounter[s[L]]-=1
          L+=1
        return res
        