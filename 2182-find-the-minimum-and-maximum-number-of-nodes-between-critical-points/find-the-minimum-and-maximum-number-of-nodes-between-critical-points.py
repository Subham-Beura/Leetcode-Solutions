# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=head.next
        if not head.next.next:
            return [-1,-1]
        next=head.next.next
        arr=[] 
        counter=1
        minV,maxV=10e5,0
        while next:
            # Local Maxima or local maxima
            if (prev.val<curr.val and curr.val>next.val) or (prev.val>curr.val and curr.val<next.val):
                # print(f"{curr.val} {counter}")
                if arr!=[]:
                    minV=min(minV,counter-arr[-1])
                arr.append(counter)
            # Increment window
            counter+=1
            prev=curr
            curr=next
            next=next.next
        if len(arr)<2:
            return [-1,-1]
        return [minV,arr[-1]-arr[0]] 
