class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        self.mem = [[False for i in range(len(nums))] for i in range(len(nums))]
        self.nums = nums
        if self.helper(0, len(nums) - 1) >= 0:
            return True
        return False

    def helper(self, s, e):
        if self.mem[s][e] == False:
            if s == e:
                self.mem[s][e] = self.nums[s]
            else:
                self.mem[s][e] = max(self.nums[s] - self.helper(s + 1, e), self.nums[e] - self.helper(s, e - 1))
        return self.mem[s][e]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.PredictTheWinner([2,4,55,6,8])