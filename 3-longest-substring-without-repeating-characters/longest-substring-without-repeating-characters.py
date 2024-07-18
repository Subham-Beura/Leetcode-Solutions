class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,R=0,0
        n=len(s)
        found=set()
        maxV=0
        while L<n and R<n:
            if s[R] in found:
                while s[R] in found:
                    found.remove(s[L])
                    L+=1
            else:
                maxV=max(R-L+1,maxV)
            found.add(s[R])
            R+=1
        return maxV
