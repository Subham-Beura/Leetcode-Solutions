class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathList=path.split('/')
        stack=[]
        for e in pathList:
          if e=="" or e=='.':
            continue
          if e=='..':
            if len(stack)!=0:
              stack.pop()
            continue
          stack.append(e)
        res=""
        if stack==[]:
          return "/"
        for dir in stack:
          res+='/'
          res+=dir
        return res 

          
        