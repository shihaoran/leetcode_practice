class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        for n in nums:
            s, e = 0, len(l) - 1
            while s <= e:
                m = (s + e) >> 1
                if l[m] >= n:
                    e = m - 1
                else:
                    s = m + 1
            if s >= len(l):
                l.append(n)
            else:
                l[s] = n
        return len(l)

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.lengthOfLIS([10,9,2,5,3,7,101,18])