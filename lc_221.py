import math
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        _l = len(matrix[0])
        _h = len(matrix)
        _max = 0
        for i in range(_l):
            _max = max(_max, int(matrix[0][i]))
        for i in range(_h):
            _max = max(_max, int(matrix[i][0]))
        for i in range(1, _h):
            for j in range(1, _l):
                if int(matrix[i-1][j-1]) > 0 and int(matrix[i][j]) > 0:
                    root = int(math.sqrt(float(matrix[i-1][j-1])))
                    _root = 0
                    for k in range(1, root+1):
                        if matrix[i][j-k] == '0' or matrix[i-k][j] == '0':
                            break
                        _root = k
                    matrix[i][j] = (_root+1)*(_root+1)
                    _max = max(_max, matrix[i][j])
        return _max



if __name__ == '__main__':
    # begin
    s = Solution()
    print s.maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]])