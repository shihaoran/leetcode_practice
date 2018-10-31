class NumArray(object):
    n = [0]

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = [0]
        if len(nums) != 0:
            self.n.append(nums[0])
            for i in range(1, len(nums)):
                self.n.append(self.n[i] + nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.n[j + 1] - self.n[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    # begin
    s = NumArray([1])
    print s.sumRange(0,0)