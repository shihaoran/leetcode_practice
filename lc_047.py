class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set([])
        self.helper('', nums, res)
        res1 = []
        for l in res:
            temp = l.split(',')
            temp1 = []
            for i in temp:
                if i == '':
                    continue
                temp1.append(int(i))
            res1.append(temp1)
        return res1

    def helper(self, step, set, res):
        if len(set) == 0:
            res.add(step[:])
            return
        for i in range(len(set)):
            temp = step[:]
            temp += ',' + str(set[i])
            self.helper(temp, set[:i] + set[i + 1:], res)

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.permuteUnique([-1,-1,3])