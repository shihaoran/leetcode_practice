# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        left = head
        for i in range(m):
            left = left.next

        cur = left.next
        pre = left
        first = left.next

        for i in range(n - m):
            n = cur.next
            cur.next = pre
            pre = cur
            cur = n

        left.next = pre


if __name__ == '__main__':
    # begin
    s = Solution()