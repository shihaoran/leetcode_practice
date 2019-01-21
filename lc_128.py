class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums = set(nums)

        maxLen = 1

        for n in nums:
            if n -1 in nums:
                continue
            cur = 1
            while n + cur in nums:
                cur += 1
            maxLen = max(maxLen, cur)
        return maxLen


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.longestConsecutive([])