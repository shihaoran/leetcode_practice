class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper([], nums, res)
        return res

    def helper(self, step, set, res):
        if len(set) == 0:
            res.append(step[:])
            return
        for i in range(len(set)):
            temp = step[:]
            temp.append(set[i])
            self.helper(temp, set[:i] + set[i + 1:], res)

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.permute([1,2,3])