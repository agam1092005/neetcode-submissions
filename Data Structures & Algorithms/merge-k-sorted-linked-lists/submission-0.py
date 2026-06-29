# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        L = []
        for i in lists:
            while i:
                L.append(i.val)
                i = i.next
        
        L.sort()

        head = ListNode(0)
        curr = head
        for node in L:
            curr.next = ListNode(node)
            curr = curr.next
        
        return head.next