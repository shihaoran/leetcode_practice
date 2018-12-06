class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(p))] for i in range(len(s)+1)]
        if len(p) == 0 and len(s) > 0:
            return False
        if len(p) == 0 and len(s) == 0:
            return True
        if len(s) == 0 and len(p) > 0:
            for i in p:
                if i != '*':
                    return False
        if p[0] == '*':
            for i in range(len(s)+1):
                dp[i][0] = True
        elif p[0] == '?':
            dp[1][0] = True
        elif p[0] == s[0]:
            dp[1][0] = True
        else:
            return False
        for j in range(1, len(p)):
            f = False
            if p[j] == '*' and dp[0][j-1] == True:
                dp[0][j] = True
            for i in range(1, len(s)+1):
                if dp[i-1][j-1] or p[j] == '*' and dp[i][j-1]:
                    if p[j] == '*':
                        for k in range(i, len(s) + 1):
                            dp[k][j] = True
                            f = True
                        break
                    elif p[j] == '?':
                        dp[i][j] = True
                        f = True
                    elif p[j] == s[i-1]:
                        dp[i][j] = True
                        f = True
            if not f:
                return False
        return dp[-1][-1]

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.isMatch("m","**m*")