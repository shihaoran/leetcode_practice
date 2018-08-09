class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum = 0
        dic = {0:-1}
        for i in range(len(nums)):
            sum += nums[i]
            if k != 0:
                sum %= k
            if dic.has_key(sum):
                pre = dic[sum]
                if i - pre > 1:
                    return True
            else:
                dic[sum] = i
        return False


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.checkSubarraySum([0,0], 0)