class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1

        l = [len(s)] * 26
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if l[idx] == len(s):
                l[idx] = i
            else:
                l[idx] = len(s) + 1

        l.sort()

        if l[0] >= len(s):
            return -1
        return l[0]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.firstUniqChar("cc")