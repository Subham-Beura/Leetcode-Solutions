class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache={}
        def findDistinct(si,ti):
            if ti==len(t):
                return 1
            if si==len(s):
                return 0
            if (si,ti) in cache:
                return cache[(si,ti)]
            
            if s[si]==t[ti]:
                cache[(si,ti)]=findDistinct(si+1,ti+1)+findDistinct(si+1,ti)
            else:
                cache[(si,ti)]=findDistinct(si+1,ti)
            return cache[(si,ti)]
        return findDistinct(0,0)
                   