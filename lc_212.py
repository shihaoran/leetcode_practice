class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.w = len(board[0])
        self.h = len(board)
        self.board = board

        return_list = []

        for i in range(self.h):
            for j in range(self.w):
                for idx, val in enumerate(words):
                    if self.find(i, j, val, []):
                        return_list.append(val)
                        del words[idx]
        return return_list

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
    print s.findWords([['o','a','a','n'], ['e','t','a','e'], ['i','h','k','r'], ['i','f','l','v']], ["oath","pea","eat","rain"])