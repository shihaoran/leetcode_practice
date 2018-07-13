class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.list.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        list_copy = self.list[:]
        list_copy.sort()
        return list_copy[0]

if __name__ == '__main__':
    # begin
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    s.getMin()
    s.pop()
    s.top()
    s.getMin()