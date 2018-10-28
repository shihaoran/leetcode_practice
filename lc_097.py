class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True
        if len(s1) == 0 and s2 == s3:
            return True
        if len(s2) == 0 and s1 == s3:
            return True
        if sorted(s1 + s2) != sorted(s3):
            return False
        dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

        for i in range(len(s1)):
            if s1[i] != s3[i]:
                break
            else:
                dp[i+1][0] = 1
        for i in range(len(s2)):
            if s2[i] != s3[i]:
                break
            else:
                dp[0][i+1] = 1
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s3[i+j-1] and dp[i-1][j] == 1:
                    dp[i][j] = 1
                if s2[j-1] == s3[i+j-1] and dp[i][j-1] == 1:
                    dp[i][j] = 1
        if dp[-1][-1] == 1:
            return True
        else:
            return False



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")