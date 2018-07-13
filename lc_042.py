class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 1
        s = 0

        if height == []:
            return 0

        while True:
            s1 = 0
            s2 = 0
            flag = True
            flag1 = 0
            if i > height[0]:
                flag = False
            for num in height:
                if num < i:
                    if flag:
                        s2 += 1
                if num >= i:
                    flag = True
                    flag1 += 1
                    if s2 > 0:
                        s1 += s2
                        s2 = 0
            if flag1 < 3 and s1 == 0:
                break
            else:
                s += s1
                i += 1

        return s

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.trap([0,7,1,4,6])