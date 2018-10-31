import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        _max = -sys.maxint
        for i in nums:
            sum = max(i, sum+i)
            _max = max(sum, _max)
        return _max


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])