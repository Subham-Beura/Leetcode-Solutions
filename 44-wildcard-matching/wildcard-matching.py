class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def matcher(si,pi):
            if pi==len(p) and si==len(s):
                return True
            if pi==len(p) and si<len(s):
                return False
            if si==len(s) and pi<len(p):
                while si==len(s) and pi<len(p):
                    if p[pi]!="*":
                        return False
                    pi=pi+1
                return True
            if p[pi]=='*':
                return matcher(si,pi+1) or matcher(si+1,pi+1) or matcher(si+1,pi)
            if p[pi]=='?' or s[si]==p[pi]:
                return matcher(si+1,pi+1)
            return  False
        return matcher(0,0)
