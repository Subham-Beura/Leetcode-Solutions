class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i,j=0,0
        n1,n2=len(nums1),len(nums2)
        res=[]
        while i<n1 and j<n2:
            while j<n2 and nums2[j]<nums1[i]:
                j+=1
            if j==n2:
                return res
            if nums1[i]!=nums2[j]:
                i+=1
                continue 
            res.append(nums1[i])
            i+=1
            j+=1
        return res