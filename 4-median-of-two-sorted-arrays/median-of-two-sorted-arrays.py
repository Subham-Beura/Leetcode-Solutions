class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # Ensure A is the smaller one
        if len(A) > len(B):
            A, B = B, A

        n = len(A) + len(B)
        half = n // 2

        l, r = 0, len(A) - 1

        while True:
            # Last Index of leftPart of A
            i = (l + r) // 2
            # (i+1) is the length of leftPart of A
            # half-(i+1) is length of leftPart of B
            # half-(i+1)-1 is the last index of left part of B
            j = half - (i + 1) - 1

            # W.R.T barrier
            ALeft = A[i]      if i >= 0 else float("-inf")
            ARight = A[i + 1] if i + 1 < len(A) else float("inf")

            BLeft = B[j]      if j >= 0 else float("-inf")
            BRight = B[j + 1] if j + 1 < len(B) else float("inf")

            if ALeft <= BRight and BLeft <= ARight:
                # Odd
                if n % 2 == 1:
                    return min(ARight, BRight)
                # Even
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            if ALeft > BRight:
                r = i - 1
            else:
                l = i + 1
