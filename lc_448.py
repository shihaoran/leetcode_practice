class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final = []
        for index, num in enumerate(nums):
            i = abs(num) - 1
            nums[i] = -abs(nums[i])

        for index in range(len(nums)):
            if nums[index] > 0:
                final.append(index + 1)

        return final

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.findDisappearedNumbers([4,3,2,7,8,2,3,1])