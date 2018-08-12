class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets == 1 and minutesToTest/minutesToDie == 1:
            return 0
        p = 1
        num = 1
        while num * (minutesToTest/minutesToDie+1) < buckets:
            num *= (minutesToTest / minutesToDie + 1)
            p += 1
        return p


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.poorPigs(125,15,60)