class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[] 
        count=0
        arr=[0]*(len(s))
        for i,c in enumerate(s):
            if c==')' and stack :
                arr[stack.pop()]=1
                arr[i]=1
                continue
            if c=='(':
                stack.append(i)
        maxCount=0 
        for a in arr:
            if a==0:
                count=0
            else:
                count+=1
                maxCount=max(maxCount,count)
        return maxCount
        