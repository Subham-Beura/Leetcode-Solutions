class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for c in s:
            if c !=')':
                stack.append(c)
                continue
            i=len(stack)-1
            q=deque()
            while stack and i>=0 and stack[i]!='(':
                k=stack.pop()
                q.append(k)  
                i-=1
            stack.pop()
            for k in q:
                stack.append(k)
            # print(stack)
        return ''.join(str(e) for e in stack)