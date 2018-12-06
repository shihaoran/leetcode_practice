class Solution(object):
    arr = []
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.arr = nums
        res = []
        self.helper(0, [], res)
        return res

    def helper(self, s, step, result):
        if s == len(self.arr):
            result.append(step[:])
            return
        step.append(self.arr[s])
        tempStep = step[:]
        self.helper(s+1, step, result)
        step = tempStep[:-1]
        self.helper(s+1, step, result)



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.subsets([1,2,3])