class Solution(object):
    def g1(self, s1, s2):
        """
        :type s: str
        :rtype: int
        """
        s1 = sorted(s1)
        s2 = sorted(s2)
        m = 0
        cur = 0
        p1 = 0
        p2 = 0
        for i in range(2*(len(s1))):
            if p1 < len(s1) and s1[p1] < s2[p2]:
                cur += 1
                p1 += 1
            else:
                cur -= 1
                p2 += 1
            m = max(cur, m)
        return m





if __name__ == '__main__':
    # begin
    s = Solution()
    print s.g1([0, 5, 10], [30, 10, 20])