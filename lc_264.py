class NumArray(object):
    n = [0]
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n.append(nums[0])
        for i in range(len(nums)):
            self.n.append(self.n[i-1] + nums[i])


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.n[j+1] - self.n[i]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.nthUglyNumber(10)