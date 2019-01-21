class Solution(object):
    dic = {}

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        i = 1
        for c in order:
            self.dic[c] = i
            i += 1
        for i in range(len(words)):
            for j in range(i, len(words)):
                if not self.compare(words[i], words[j]):
                    return False
        return True

    def compare(self, s1, s2):
        i = 0
        while(i < len(s1) and i < len(s2)):
            if self.dic[s1[i]] > self.dic[s2[i]]:
                return False
            elif self.dic[s1[i]] < self.dic[s2[i]]:
                return True
            i += 1
        if len(s1) > len(s2):
            return False
        return True





if __name__ == '__main__':
    # begin
    s = Solution()

    print s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")