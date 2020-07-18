# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        first = head
        second = head

        for i in range(0, n):
            first = first.next
            if first is None:
                head = head.next
                return head

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head
