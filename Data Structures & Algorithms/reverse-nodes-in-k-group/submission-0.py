# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        L = []
        curr = head
    
        while curr:
            L.append(curr.val)
            curr = curr.next
        
        ans = []
        i = 0
        while i < len(L):
            arr = (L[i:i+k])
            if len(arr) < k:
                ans.extend(arr)
            else:
                ans.extend(arr[::-1])

            i += k

        head = ListNode(0)
        curr = head
        for node in ans:
            curr.next = ListNode(node)
            curr = curr.next
        
        return head.next