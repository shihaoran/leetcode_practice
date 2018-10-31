class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        if len(s) == 0:
            return res
        if len(s) == 1:
            return s

        dp = [[0 for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            for j in range(i, -1, -1):
                if s[j] == s[i] and (j+1 >= i-1 or dp[j+1][i-1] == 1):
                    dp[j][i] = 1
                    if i-j+1 > len(res):
                        res = s[j:i+1]
        return res


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.longestPalindrome("cbbd")