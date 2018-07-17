class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum = [0] * (len(num1) + len(num2) + 1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                p = int(num1[len(num1)-i-1]) * int(num2[len(num2)-j-1])
                sum[i + j + 1] += p / 10
                sum[i + j] += p % 10

        add = 0
        for i in range(len(sum)):
            s = sum[i] + add
            sum[i] = s % 10
            add = s / 10

        r = ''
        f = False
        for i in range(len(sum)):
            s = str(sum[len(sum) - i -1])
            if s == '0' and f:
                r += s
            elif s != '0':
                f = True
                r += s

        if r == '':
            return '0'
        return r

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.multiply("98","9")