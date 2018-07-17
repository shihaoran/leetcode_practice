# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        cur1 = head
        cur2 = head

        while cur1 != None and cur2 != None:
            cur1 = cur1.next
            if cur2.next != None:
                cur2 = cur2.next.next
            else:
                return False

            if cur1 == cur2:
                return True

        return False