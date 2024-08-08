class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen=0
        maxPalin=""
        for i,c in enumerate(s):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>maxLen:
                    maxLen=r-l+1
                    maxPalin=s[l:r+1]
                l-=1
                r+=1
            # Even Palindromes
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>maxLen:
                    maxLen=r-l+1
                    maxPalin=s[l:r+1]
                l-=1
                r+=1
        return maxPalin
            