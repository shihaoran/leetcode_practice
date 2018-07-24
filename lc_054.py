class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        l_bound = 0
        r_bound = len(matrix[0]) - 1
        b_bound = len(matrix) - 1
        u_bound = 0
        r_list = []
        while l_bound <= r_bound and u_bound <= b_bound:
            for i in range(l_bound, r_bound + 1):
                r_list.append(matrix[u_bound][i])

            u_bound += 1

            for i in range(u_bound, b_bound + 1):
                r_list.append(matrix[i][r_bound])

            r_bound -= 1

            for i in range(r_bound, l_bound - 1, -1):
                if u_bound > b_bound:
                    break
                r_list.append(matrix[b_bound][i])

            b_bound -= 1

            for i in range(b_bound, u_bound - 1, -1):
                if l_bound > r_bound:
                    break
                r_list.append(matrix[i][l_bound])

            l_bound += 1

        return r_list

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.spiralOrder([[1,2],[3,4]])