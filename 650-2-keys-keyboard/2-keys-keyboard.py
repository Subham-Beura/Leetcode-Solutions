class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache={}
        def minOps(s,buffer):
            if (s,buffer) in cache:
                print("hit")
                return cache[(s,buffer)]
            i=len(s)
            if i==n:
                cache[(s,buffer)]=0
                return 0
            
            copyPaste,pasteAgain=1000,1000
            # Paste current buffer again
            if len(s+buffer)<=n and buffer!="":
                pasteAgain=minOps(s+buffer,buffer)+1
            # Copy and Paste two step which cannot be interrupted
            if len(s+s)<=n:
                copyPaste=minOps(s+s,s)+2
            cache[(s,buffer)]= min(pasteAgain,copyPaste)
            return cache[s,buffer]
        return minOps("A","")