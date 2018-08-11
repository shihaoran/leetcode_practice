import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            d[x][x] = d[y][y] = 1.0
            d[x][y] = val
            d[y][x] = 1 / val
        for k in d:
            for i in d[k]:
                for j in d[k]:
                    d[i][j] = d[i][k] * d[k][j]
        return [d[x].get(y, -1.0) for x, y in queries]



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])