# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L1=0
        L2=0
        place=0
        while l1 and l2:
          L1=L1+l1.val*(10**place)
          L2=L2+l2.val*(10**place)
          l1=l1.next
          l2=l2.next
          place+=1
        while l1:
          L1=L1+l1.val*(10**place)
          l1=l1.next
          place+=1
        while l2:
          L2=L2+l2.val*(10**place)
          l2=l2.next
          place+=1
        sum=L1+L2
        l3=ListNode(0)
        res=l3
        while sum:
          l3.val=sum%10
          sum=sum/10
          if sum:
            l3.next=ListNode(0)
            l3=l3.next
        return res 