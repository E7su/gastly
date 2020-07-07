class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        while cur:
            if getattr(cur, 'visited', False):
                return True
            setattr(cur, 'visited', True)
            cur = cur.next
        return False
