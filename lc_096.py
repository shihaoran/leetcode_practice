class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 2]
        for i in range(3, n+1):
            s = 0
            for j in range(i):
                s += dp[j]*dp[i-j-1]
            dp.append(s)
        return dp[n]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.numTrees(3)