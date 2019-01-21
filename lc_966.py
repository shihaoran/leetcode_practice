class Solution(object):
    set = ['a', 'e', 'i', 'o', 'u']

    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        res = []
        for i in queries:
            flag = False
            if i in wordlist:
                res.append(i)
            else:
                for j in wordlist:
                    if self.helper(j, i):
                        flag = True
                        res.append(j)
                        break
                if not flag:
                    res.append('')
        return res

    def helper(self, w, q):
        if len(w) != len(q):
            return False
        for i in range(len(w)):
            s1 = w[i].lower()
            s2 = q[i].lower()
            if s1 != s2:
                if s1 not in self.set or s2 not in self.set:
                    return False
        return True





if __name__ == '__main__':
    # begin
    s = Solution()

    print s.spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])