# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = self.findMiddle(head)
        previous, current = self.reverseSecondPart(slow)
        is_equal = self.compareFrontAndBack(previous, head)
        return is_equal
    
    """
    Find the middle of the list
    """
    def findMiddle(self, head: ListNode):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow, fast
    
    """
    Reverse second part of the list
    """
    def reverseSecondPart(self, slow):
        previous = slow
        current = slow.next
        previous.next = None
        while current:
            tmp_next = current.next
            current.next = previous
            previous = current
            current = tmp_next
        return previous, current

    """
    Compare the front and back of the list
    """
    def compareFrontAndBack(self, previous, head):
        reverse = previous
        forward = head
        while reverse and forward:
            if forward.val != reverse.val:
                return False
            reverse = reverse.next
            forward = forward.next      
        return True
