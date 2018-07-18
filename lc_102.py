# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        this_layer = []
        next_layer = []
        val_list = []

        if not root:
            return []

        this_layer.append(root)

        while len(this_layer) > 0:
            layer_list = []
            next_layer = []
            for i in this_layer:
                layer_list.append(i.val)
                if i.left:
                    next_layer.append(i.left)
                if i.right:
                    next_layer.append(i.right)
            this_layer = next_layer
            val_list.append(layer_list)

        return val_list


if __name__ == '__main__':
    # begin
    s = Solution()