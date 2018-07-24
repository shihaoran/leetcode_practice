class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        sum = 0
        min = len(nums) + 1
        i = 0
        j = 0
        while i < len(nums):
            sum += nums[i]

            while sum - nums[j] >= s:
                sum -= nums[j]
                j += 1

            if sum >= s and i - j < min:
                min = i - j + 1
            i += 1
        if min < len(nums) + 1:
            return min
        return 0

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.minSubArrayLen(7, [2,3,1,2,4,3])