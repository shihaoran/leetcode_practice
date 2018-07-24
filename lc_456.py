import sys

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) < 3:
            return False
        a3 = -sys.maxint
        s = []
        for i in range(len(nums)):
            if nums[len(nums) - i - 1] < a3:
                return True
            else:
                while len(s) > 0 and nums[len(nums) - i - 1] > s[-1]:
                    a3 = s[-1]
                    del s[-1]
            s.append(nums[len(nums) - i - 1])

        return False


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.find132pattern([1,2,3,4])