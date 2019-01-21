class Solution(object):
    arr = []
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.arr = sorted(nums)
        res = []
        self.helper(0, [], res)
        return res

    def helper(self, s, step, result):
        if s == len(self.arr):
            result.append(step[:])
            return
        count = 0
        while s + count + 1 < len(self.arr) and self.arr[s+count+1] == self.arr[s]:
            count += 1
        self.helper(s + count + 1, step[:], result)
        for i in range(count+1):
            step.append(self.arr[s])
            self.helper(s + count + 1, step[:], result)



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.subsetsWithDup([1,2,2])