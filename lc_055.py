class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, maxIndex = 0, 0
        while i < len(nums) and i <= maxIndex:
            maxIndex = max(i + nums[i], maxIndex)
            i += 1
        if maxIndex < len(nums)-1:
            return False
        return True


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.canJump([1])