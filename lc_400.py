class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        sum = 0
        num = 9
        while True:
            if sum + num * i >= n:
                break
            sum += num * i
            num *= 10
            i += 1

        a = (n - sum) / i
        b = (n - sum) % i
        while b == 0:
            b = i
            a -= 1

        c = num / 9 + a
        l = []
        while c:
            l.append(c % 10)
            c /= 10

        return l[-b]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.findNthDigit(11)