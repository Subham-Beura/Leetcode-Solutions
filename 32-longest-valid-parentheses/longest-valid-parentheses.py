class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[] 
        count=0
        arr=[0]*(len(s))
        for i,c in enumerate(s):
            # print(i)
            # print(c)
            # print(stack)
            # print(arr)
            if c==')' and stack :
                arr[stack[-1]]=1
                arr[i]=1
                stack.pop()
                continue
            if c=='(':
                stack.append(i)
        # print(arr)
        maxCount=0 
        for a in arr:
            if a==0:
                count=0
            else:
                count+=1
                maxCount=max(maxCount,count)
        return maxCount
        