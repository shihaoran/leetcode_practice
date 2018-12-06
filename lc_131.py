class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(0, [], res, s)
        return res

    def helper(self, s, step, result, str):
        if s == len(str):
            result.append(step[:])
            return
        for i in range(s+1, len(str)+1):
            if self.isPalindrome(str[s:i]):
                step.append(str[s:i])
                self.helper(i, step[:], result, str)
                step = step[:-1]

    def isPalindrome(self, str):
        s, e = 0, len(str)-1
        while s < e:
            if str[s] != str[e]:
                return False
            s += 1
            e -= 1
        return True

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.partition("")