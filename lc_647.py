class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count = 0
        for i in range(len(s)):
            self.find(s, i, i)
            self.find(s, i, i+1)
        return self.count

    def find(self, str, s, e):
        while s >= 0 and e < len(str) and str[s] == str[e]:
            self.count += 1
            s -= 1
            e += 1


if __name__ == '__main__':
    # begin
    s = Solution()

    print s.countSubstrings('aaa')