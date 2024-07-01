# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        stack=[]
        if not head:
            return None
        while curr:
            stack.append(curr)
            curr=curr.next
        head=stack.pop()
        curr=head
        while stack:
            node=stack.pop()
            curr.next=node
            node.next=None
            curr=curr.next
        return head