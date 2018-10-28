class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        dp = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
        dp[0][0] = grid[0][0]

        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for i in range(1, len(grid[0])):
            dp[0][i] = grid[0][i] + dp[0][i-1]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

        return dp[-1][-1]

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])