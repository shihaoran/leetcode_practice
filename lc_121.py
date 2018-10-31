class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        k = 1
        dp = [[0 for i in range(len(prices))] for i in range(k+1)]

        for i in range(1, k+1):
            maxProfit = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j] + maxProfit)
                maxProfit = max(maxProfit, dp[i-1][j] - prices[j])
        return dp[-1][-1]

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.maxProfit([7,1,5,3,6,4])