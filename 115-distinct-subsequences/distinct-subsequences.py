class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def findDistinct(si,ti):
            if ti==len(t):
                return 1
            if si==len(s):
                return 0
            
            if s[si]==t[ti]:
                return findDistinct(si+1,ti+1)+findDistinct(si+1,ti)
            return findDistinct(si+1,ti)

        return findDistinct(0,0)
                   