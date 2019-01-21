class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix = zip(*matrix)
        l = len(matrix)
        for i in range(l):
            i = list(matrix[i])
            i.reverse()
            matrix.append(i)
            del matrix[0]
        return matrix

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])