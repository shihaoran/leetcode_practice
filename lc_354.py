class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def s(x, y):
            return -1 if (x[0] < y[0] or x[0] == y[0] and x[1] > y[1]) else 1

        envelopes.sort(cmp=s)
        l = []
        for n in envelopes:
            s, e = 0, len(l) - 1
            while s <= e:
                m = (s + e) >> 1
                if l[m] >= n[1]:
                    e = m - 1
                else:
                    s = m + 1
            if s >= len(l):
                l.append(n[1])
            else:
                l[s] = n[1]
        return len(l)

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])