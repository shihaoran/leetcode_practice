# Definition for a binary tree node.
# class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self._genTrees(1, n+1)

    def _genTrees(self, s, e):
        res = []
        if s == e:
            return None
        for i in range(s, e):
            for j in self._genTrees(s, i) or [None]:
                for k in self._genTrees(i + 1, e) or [None]:
                    r = TreeNode(i)
                    r.left = j
                    r.right = k
                    res.append(r)
        return res




if __name__ == '__main__':
    # begin
    s = Solution()
    print s.generateTrees(4)