class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arr=nums

        # Edge Cases
        if len(arr)==1:
          return 0 if target==arr[0] else -1

        l,r=0,len(nums)-1
        while l<r:
          mid=(r+l)/2
          if arr[r]==target:
            return r
          if arr[l]==target:
            return l
          if arr[mid]==target:
            return mid
          if arr[mid] > arr[r]:
            # large Side
            if target <arr[l] or target>arr[mid]:
              l=mid+1
            else:
              r=mid-1
          elif arr[mid] < arr[l]:
            # Small Side
            if target< arr[mid] or target> arr[l]:
              r=mid-1
            else:
              l=mid+1
          else:
            if target > arr[mid]:
              l=mid+1
            else:
              r=mid-1
        return -1
           
          