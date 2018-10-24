class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """

        l = len(A)
        m = 0

        for i in range(2*l-1):
            for j in range(2*l-1):
                sum = 0
                if i - l + 1 <= 0:
                    xs = 0
                    xe = i + 1
                else:
                    xs = i - l + 1
                    xe = l
                if j - l + 1 <= 0:
                    ys = 0
                    ye = j + 1
                else:
                    ys = j - l + 1
                    ye = l
                for x in range(xs, xe):
                    for y in range(ys, ye):
                        _x = x-i+l-1
                        _y = y-j+l-1
                        if B[x][y] == A[_x][_y] and B[x][y] == 1:
                            sum += 1
                if sum > m:
                    m = sum
        return m



if __name__ == '__main__':
    # begin
    s = Solution()

    print s.largestOverlap([[1,1,0],
            [0,1,0],
            [0,1,0]],
            [[0,0,0],
            [0,1,1],
            [0,0,1]])