class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(self._rob(0, len(nums)-2, nums), self._rob(1, len(nums)-1, nums))

    def _rob(self, s, e, nums):
        _i = 0
        _e = 0
        for i in range(s, e+1):
            include, exclude = _i, _e
            _i = _e + nums[i]
            _e = max(include, exclude)
        return max(_i, _e)


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.rob([0,0,1])