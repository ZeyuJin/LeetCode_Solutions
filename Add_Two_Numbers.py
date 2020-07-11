# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        head = ListNode()
        tail = head
        
        # compute the first digit
        tail.val = (curr1.val + curr2.val) % 10
        carri = floor((curr1.val + curr2.val) / 10)
        curr1 = curr1.next
        curr2 = curr2.next
        
        
        # loop over other digits
        while curr1 != None and curr2 != None:
            newhead = ListNode()
            newhead.val = (carri + curr1.val + curr2.val) % 10
            carri = floor((carri + curr1.val + curr2.val) / 10)
            tail.next = newhead
            tail = newhead
            
            curr1 = curr1.next
            curr2 = curr2.next
            
        p2 = curr1  if curr1 != None  else curr2
        while p2 != None:
            newhead = ListNode(val=carri)
            newhead.val = (carri + p2.val) % 10
            carri = floor((carri + p2.val) / 10)
            tail.next = newhead
            tail = newhead
            p2 = p2.next
            
        if carri > 0:
            newhead = ListNode(val=carri)
            tail.next = newhead
            tail = newhead

        return head
