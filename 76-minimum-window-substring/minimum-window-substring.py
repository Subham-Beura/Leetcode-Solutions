class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        if s in t:
            return ""
        if t in s:
            return t
        countSet=Counter(t)
        charSet={c:0 for c in t}
        R=0
        L=0
        ans=""
        resLen=9999999
        while R<len(s):
            if s[R] in t:
                charSet[s[R]]+=1
            while self.isWindow(s[L:R+1],charSet,countSet):
                if R-L+1<resLen:
                    ans=s[L:R+1]
                    resLen=R-L+1
                if s[L] in charSet:
                    charSet[s[L]]-=1
                L+=1
            R+=1
        return ans
    def isWindow(self,s,charSet,countSet):
        for c in countSet:
            if charSet[c]<countSet[c]:
                return False
        return True