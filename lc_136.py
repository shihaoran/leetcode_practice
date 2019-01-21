class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for n in nums:
            try:
                m.pop(n)
            except:
                m[n] = 1
        return m.popitem()[0]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.singleNumber([2,2,1])