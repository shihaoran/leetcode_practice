class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.w = len(board[0])
        self.h = len(board)
        self.board = board

        for i in range(self.h):
            for j in range(self.w):
                if self.find(i, j, word, []):
                    return True
        return False

    def find(self, i, j, word, path):
        if word == '':
            return True
        if i < 0 or i >= self.h or j < 0 or j >= self.w:
            return False
        if word[0] != self.board[i][j]:
            return False
        if (i, j) in path:
            return False
        path.append((i, j))
        if self.find(i - 1, j, word[1:], path[:]):
            return True
        if self.find(i + 1, j, word[1:], path[:]):
            return True
        if self.find(i, j - 1, word[1:], path[:]):
            return True
        if self.find(i, j + 1, word[1:], path[:]):
            return True


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")