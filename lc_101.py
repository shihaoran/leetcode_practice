# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        this_layer = []
        next_layer = []
        val_list = []

        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False

        this_layer.append(root.left)
        this_layer.append(root.right)

        while len(this_layer) > 0:
            layer_list = []
            next_layer = []
            f = False
            for i, node in enumerate(this_layer):
                if i < len(this_layer) / 2:
                    if node and node.val:
                        layer_list.append(node.val)
                    else:
                        layer_list.append(False)
                else:
                    v = layer_list.pop()
                    if node and node.val:
                        if v != node.val:
                            return False
                    else:
                        if v:
                            return False
                if node and node.left:
                    f = True
                    next_layer.append(node.left)
                else:
                    next_layer.append(False)
                if node and node.right:
                    f = True
                    next_layer.append(node.right)
                else:
                    next_layer.append(False)
            if not f:
                break
            this_layer = next_layer

        return True


if __name__ == '__main__':
    # begin
    s = Solution()