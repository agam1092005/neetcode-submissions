# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        c = 0
        while l1 or l2 or c:
            if l1:
                a = l1.val
            else:
                a = 0
            
            if l2:
                b = l2.val
            else:
                b = 0

            new_val = a + b + c
            c = new_val // 10
            new_val = new_val % 10
            curr.next = ListNode(new_val)

            curr = curr.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            
            if l2:
                l2 = l2.next
            else:
                l2 = None
        
        return head.next