# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    val = 0
    hasValue = False
    res = True

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.helper(root)
        return self.res

    def helper(self, cur):
        if cur != None:
            if self.hasValue:
                if cur.val != self.val:
                    self.res = False
            self.hasValue = True
            self.val = cur.val
            self.helper(cur.left)
            self.helper(cur.right)





if __name__ == '__main__':
    # begin
    s = Solution()

    print s.minDeletionSize(["xc","yb","za"])