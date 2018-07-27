class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = list(range(1005))

        def find(f):
            if f != parent[f]:
                parent[f] = find(parent[f])
            return parent[f]

        for f, t in edges:
            if find(f) == find(t):
                return [f, t]
            else:
                parent[find(f)] = find(t)
        return []


if __name__ == '__main__':
    # begin
    s = Solution()

    print s.findRedundantConnection([[1,2], [1,3], [2,3]])