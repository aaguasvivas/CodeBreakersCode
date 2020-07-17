# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        lista = headA
        listb = headB

        while lista != listb:
            lista = headB if lista is None else lista.next
            listb = headA if listb is None else listb.next
        return lista
