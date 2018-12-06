class Solution(object):
    def findMaxGoalsProbability(self, teamGoals):
        if len(teamGoals) == 0:
            return '0.00'
        teamCnt = teamGoals[0]
        maxScore = -1
        scoreDic = {}
        for i in range(1, len(teamGoals)):
            for j in range(i + 1, len(teamGoals)):
                scoreSum = teamGoals[i] + teamGoals[j]
                if scoreDic.has_key(scoreSum):
                    scoreDic[scoreSum] += 1
                else:
                    scoreDic[scoreSum] = 1
                maxScore = max(scoreSum, maxScore)
        return self.round2(float(scoreDic[maxScore]) / float((teamCnt * (teamCnt - 1))) * 2.00)

    def round2(self, res):
        res_x, res_y = str(res).split('.')
        return res_x + '.' + res_y[0:2]





if __name__ == '__main__':
    # begin
    s = Solution()
    print s.findMaxGoalsProbability([3,1,3,1])