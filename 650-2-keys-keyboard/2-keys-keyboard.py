class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def minOps(s,buffer):
            i=len(s)
            if i==n:
                return 0
            
            copyPaste,pasteAgain=1000,1000
            if len(s+buffer)<=n and buffer!="":
                pasteAgain=minOps(s+buffer,buffer)+1
            if len(s+s)<=n:
                copyPaste=minOps(s+s,s)+2
            return min(pasteAgain,copyPaste)
        return minOps("A","")