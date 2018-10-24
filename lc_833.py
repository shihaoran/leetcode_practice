class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        offset = 0
        indexList = sorted(range(len(indexes)), key=lambda k: indexes[k])
        for i in range(len(indexList)):
            flag = True
            start = indexes[indexList[i]]
            for j in range(len(sources[indexList[i]])):
                if S[start+offset+j] != sources[indexList[i]][j]:
                    flag = False
            if flag:
                S = S[:start+offset] + targets[indexList[i]] + S[start+offset+len(sources[indexList[i]]):]
                offset += len(targets[indexList[i]]) - len(sources[indexList[i]])
        return S

if __name__ == '__main__':
    # begin
    s = Solution()

    print s.findReplaceString("jjievdtjfb", [4,6,1], ["md","tjgb","jf"], ["foe","oov","e"])