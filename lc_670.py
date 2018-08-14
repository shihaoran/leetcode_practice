class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        l = [-1]*10
        s_list = list(s)
        for idx, c in enumerate(s):
            c = int(c)
            l[c] = idx
        for idx, c in enumerate(s):
            c = int(c)
            for i in range(9,c,-1):
                if l[i] > idx:
                    temp = s_list[l[i]]
                    s_list[l[i]] = s_list[idx]
                    s_list[idx] = temp
                    return int(''.join(s_list))
        return int(''.join(s_list))






if __name__ == '__main__':
    # begin
    s = Solution()

    print s.maximumSwap(98368)