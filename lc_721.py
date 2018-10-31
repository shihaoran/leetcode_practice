class Solution(object):
    dicName = {}
    dicParent = {}
    dicUnion = {}
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        self.dicName = {}
        self.dicParent = {}
        self.dicUnion = {}
        res = []
        for i in accounts:
            for j in range(1, len(i)):
                self.dicName[i[j]] = i[0]
                self.dicParent[i[j]] = i[j]

        for i in accounts:
            p = self.findParent(i[1])
            for j in range(1, len(i)):
                self.dicParent[self.findParent(i[j])] = p

        for i in accounts:
            for j in range(1, len(i)):
                p = self.findParent(i[j])
                if not self.dicUnion.has_key(p):
                    self.dicUnion[p] = set([i[j]])
                elif self.dicUnion[p]:
                    self.dicUnion[p].add(i[j])

        for i in self.dicUnion.keys():
            new = sorted(list(self.dicUnion[i]))
            res.append([self.dicName[i]] + new)
        return res

    def findParent(self, s):
        while self.dicParent[s] != s:
            s = self.dicParent[s]
        return s




if __name__ == '__main__':
    # begin
    s = Solution()

    print s.accountsMerge([["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]])