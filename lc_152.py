class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        _min = nums[0]
        _max = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                _min, _max = _max, _min
            _max = max(nums[i], _max*nums[i])
            _min = min(nums[i], _min*nums[i])
            res = max(res, _max)
        return res

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.maxProduct([2,3,-2,4])