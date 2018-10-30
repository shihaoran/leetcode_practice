class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s == '0':
                return 0
            return 1
        if s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] > '2' or s[i-1] == '0':
                    return 0
                else:
                    dp.append(dp[i - 1])
            elif s[i-1] == '1' or s[i-1] == '2' and s[i] <= '6' :
                dp.append(dp[i-1]+dp[i])
            else:
                dp.append(dp[i])
        return dp[-1]



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.numDecodings("01")