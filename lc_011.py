class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        max = 0
        while j - i > 0:
            area = min(height[i], height[j])*(j-i)
            if area > max:
                max = area
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return max

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.maxArea([1,8,6,2,5,4,8,3,7])