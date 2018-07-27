class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum = 0
        if len(nums) == 0:
            return False
        for num in nums:
            sum += num
        if sum % 2 == 1:
            return False
        sum /= 2
        dp = [False] * (sum + 1)
        dp[0] = True
        for num in nums:
            if num > sum:
                continue
            for i in range(sum, num-1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[sum]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.canPartition([1,5,11,5])