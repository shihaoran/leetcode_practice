class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.isPowerOfThree(9)