class Solution(object):
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """

        parent = list(range(300))
        value = list(1 for i in range(300))

        l = len(graph)
        maxIndex = 0
        maxValue = 0
        parentToInitital = {}
        for i in range(l):
            for j in range(i+1, l):
                if graph[i][j] == 1:
                    self.joinNode(i, j, parent, value)
        initial = sorted(initial)
        for i in initial:
            p = self.findParent(i, parent)
            if value[p] > 0:
                value[p] = -value[p]
                parentToInitital[p] = i
        for i in range(l):
            if value[i] < maxValue:
                maxValue = value[i]
                maxIndex = i
        return parentToInitital[maxIndex]

    def findParent(self, n, parent):
        s = n
        while parent[n] != n:
            n = parent[n]
        parent[s] = n
        return n

    def joinNode(self, p, c, parent, value):
        parent[self.findParent(c, parent)] = self.findParent(p, parent)
        value[self.findParent(p, parent)] += 1
        return


if __name__ == '__main__':
    # begin
    s = Solution()

    print s.minMalwareSpread([[1,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,1],
                              [0,0,1,0,1,0,0,0,0,1],[0,0,0,1,0,0,0,0,0,1],
                              [0,0,1,0,1,0,1,0,0,1],[0,0,0,0,0,1,1,0,0,0],
                              [0,0,0,0,1,1,1,0,0,1],[0,0,0,0,0,0,0,1,1,0],
                              [0,0,0,0,0,0,0,1,1,0],[0,1,1,1,1,0,1,0,0,1]], [9,0,2])