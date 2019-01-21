class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, 10):
            self.helper(str(i), res, N, K)
        res1 = []
        for i in res:
            res1.append(int(i))
        if N == 1:
            res1.append(0)
        return res1

    def helper(self, step, res, N, K):
        if len(step) == N:
            res.append(step[:])
            return
        if int(step[-1]) - K >= 0:
            self.helper(step[:] + str(int(step[-1]) - K), res, N, K)
        if int(step[-1]) + K <= 9 and K != 0:
            self.helper(step[:] + str(int(step[-1]) + K), res, N, K)




if __name__ == '__main__':
    # begin
    s = Solution()

    print s.numsSameConsecDiff(1, 0)