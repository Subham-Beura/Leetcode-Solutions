class Solution(object):
    def __init__(self):
        cache={}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.cache={}
        return self.decode(s)
    def decode(self,s):
        if s in self.cache:
            return self.cache[s]
        if s=="":
            return 1
        if s[0]=="0":
            return 0
        if len(s)==1:
            return 1
        res= self.decode(s[1:])
        if s[0] =="1" or (s[0]=='2' and s[1] in "0123456"):
            res+=self.decode(s[2:])
        self.cache[s]=res
        return res
        