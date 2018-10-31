class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(m)] for i in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[-1][-1]

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.uniquePaths(7,3)