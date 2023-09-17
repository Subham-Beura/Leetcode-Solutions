class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h=height
        l,r=0,len(h)-1
        maxV=-999999
        while l<r:
          volume=min(h[l],h[r])*(r-l)
          maxV=max(maxV,volume)
          if h[l]>=h[r]:
            r-=1
          else:
            l+=1
          
        
        return maxV