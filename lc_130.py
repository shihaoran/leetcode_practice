class Solution(object):
    b = []

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not any(board):
            return
        m, n = len(board), len(board[0])
        self.b = board

        for i in range(n):
            if self.b[0][i] == 'O':
                self.expand(0, i)
            if m > 1 and self.b[m-1][i] == 'O':
                self.expand(m-1, i)
        for i in range(m):
            if self.b[i][0] == 'O':
                self.expand(i, 0)
            if n > 1 and self.b[i][n-1] == 'O':
                self.expand(i, n-1)
        for i in range(m):
            for j in range(n):
                if self.b[i][j] == 'O':
                    self.b[i][j] = 'X'
        for i in range(m):
            for j in range(n):
                if self.b[i][j] == '1':
                    self.b[i][j] = 'O'
        board = self.b
        return

    def expand(self, i, j):
        self.b[i][j] = '1'
        des = [(-1,0), (1,0), (0,-1), (0,1)]
        for d in des:
            x = i + d[0]
            y = j + d[1]
            if x < 0 or x >= len(self.b) or y < 0 or y >= len(self.b[0]):
                continue
            if self.b[x][y] == 'O':
                self.expand(x, y)


if __name__ == '__main__':
    # begin
    s = Solution()
    i = []
    s.solve(i)
    print i