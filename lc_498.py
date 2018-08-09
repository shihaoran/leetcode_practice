class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l = []
        if len(matrix) == 0:
            return l
        m, n = len(matrix), len(matrix[0])
        for i in range(m+n-1):
            if i % 2 == 1:
                s = max(0, i - n + 1)
                e = min(i + 1, m)
            else:
                s = min(i, m - 1)
                e = max(-1, i - n)
            for j in range(s, e, i%2*2-1):
                l.append(matrix[j][i-j])
        return l


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ]
])