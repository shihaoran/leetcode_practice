# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(1, n)

    def helper(self, s, e):
        m = (s + e) / 2
        r = guess(m)
        if r == 0:
            return m
        elif r == 1:
            return self.helper(m + 1, e)
        elif r == -1:
            return self.helper(s, m - 1)
