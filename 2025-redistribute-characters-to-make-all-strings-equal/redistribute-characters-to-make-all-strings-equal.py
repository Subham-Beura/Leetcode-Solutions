class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        chars={}
        for word in words:
            for c in word:
                chars[c]=chars.get(c,0)+1
        sum=0
        n=len(words)
        for k in chars.keys():
            if chars[k]%n !=0:
                return False
        return True
