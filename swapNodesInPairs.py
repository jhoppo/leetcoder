class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(f"1: {head}")
        if head is None or head.next is None:
            return head
        current = head
        while current and current.next:
            current.val, current.next.val = current.next.val, current.val
            current = current.next.next
        print(f"2: {head}")
        return head