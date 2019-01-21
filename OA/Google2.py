import heapq, math
class Solution(object):
    def g2(self, k, s1, s2):
        """
        :type s: str
        :rtype: int
        """
        l = []
        o = 0
        for i in range(len(s1)):
            heapq.heappush(l, s1[i]*s1[i] + s2[i]*s2[i])
        for i in range(k):
            o = heapq.heappop(l)
        return int(math.sqrt(o)) + 1





if __name__ == '__main__':
    # begin
    s = Solution()
    print s.g2(2, [0, 5, 10], [30, 10, 20])