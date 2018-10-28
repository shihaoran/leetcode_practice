class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        dp = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            return 0

        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1
        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])