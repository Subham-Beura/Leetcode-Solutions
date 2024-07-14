class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j=len(s)-1
        while j>=0 and s[j]==' ':
            s=s[:-1] 
            j-=1
        return len(s.split(" ")[-1])