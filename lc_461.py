class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x > y:
            temp = y
            y = x
            x = temp

        l1 = self.to2bit(x)
        l2 = self.to2bit(y)
        c = 0

        if len(l1) < len(l2):
            for i in range(len(l2) - len(l1)):
                l1.append(0)

        for i in range(len(l1)):
            if l1[i] != l2[i]:
                c += 1

        return c

    def to2bit(self, x):
        if x == 0:
            return [0]
        l = []
        while x != 0:
            l.append(x % 2)
            x -= x % 2
            x /= 2
        return l


if __name__ == '__main__':
    # begin
    s = Solution()

    print s.hammingDistance(1,4)