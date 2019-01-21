class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        m = abs(n)
        ans = 1.0
        while m:
            if m & 1:
                ans *= x
            x *= x
            m >>= 1
        return ans if n >= 0 else 1 / ans



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.myPow(2, 256)