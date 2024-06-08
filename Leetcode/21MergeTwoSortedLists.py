# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        h1 = list1
        h2 = list2
        if h1.val < h2.val:
            ret = h1
            h1 = h1.next
        else:
            ret = h2
            h2 = h2.next
        cur = ret
        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
                cur = cur.next
            else:
                cur.next = h2
                h2 = h2.next
                cur = cur.next
        if h1 is not None:
            cur.next = h1
        else:
            cur.next = h2
        return ret