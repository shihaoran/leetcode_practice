
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        sum = 0
        head = ListNode(0)
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        while len(s1) > 0 or len(s2) > 0:
            if len(s1) > 0:
                sum += s1[-1]
                del s1[-1]
            if len(s2) > 0:
                sum += s2[-1]
                del s2[-1]
            head.val = sum % 10
            new = ListNode(sum / 10)
            new.next = head
            head = new
            sum /= 10

        if head.val == 0:
            return head.next
        return head


if __name__ == '__main__':
    # begin
    s = Solution()
    v1 = 234
    v2 = 1234
    head = ListNode(0)
    while v1:
        v, v1 = v1 % 10, v1 // 10
        head.next, head.next.next = ListNode(v), head.next
    l1 = head.next
    head = ListNode(0)
    while v2:
        v, v2 = v2 % 10, v2 // 10
        head.next, head.next.next = ListNode(v), head.next
    l2 = head.next


    print s.addTwoNumbers(l1, l2)