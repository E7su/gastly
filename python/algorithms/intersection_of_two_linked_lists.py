# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        cycle_counter = 0
        while pa is not None and pb is not None:
            if pa == pb:
                return pa
            if pa.next is None:
                cycle_counter += 1
                if cycle_counter == 2:
                    return None
            pa = (pa.next if pa.next is not None else headB)
            pb = (pb.next if pb.next is not None else headA)
        
        return None
                
        
