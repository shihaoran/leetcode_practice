# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    sum = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.helper('', root)
        return self.sum

    def helper(self, step, cur):
        step += str(cur.val)
        if not cur.left or cur.right:
            self.sum += int(step)
            return
        if cur.left:
            self.helper(step, cur.left)
        if cur.right:
            self.helper(step, cur.right)


if __name__ == '__main__':
    # begin
    s = Solution()