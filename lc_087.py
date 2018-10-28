class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True
        else:
            for i in range(1, len(s1)):
                a1 = self.isScramble(s1[0:i], s2[0:i])
                a2 = self.isScramble(s1[i:], s2[i:])
                b1 = self.isScramble(s1[0:i], s2[-i:])
                b2 = self.isScramble(s1[i:], s2[0:-i])
                if (a1 and a2) or (b1 and b2):
                    return True
            return False



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.isScramble("abcde", "caebd")