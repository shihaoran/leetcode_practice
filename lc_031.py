class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 1
        j = i
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1

        while j >= i:
            if nums[j] > nums[i - 1]:
                break
            j -= 1

        if i > 0:
            nums = self.swap(i - 1, j, nums)
            return self.reverse(i, len(nums) - 1, nums)
        else:
            return self.reverse(0, len(nums) - 1, nums)

        return

    def swap(self, i, j, nums):
        t = nums[j]
        nums[j] = nums[i]
        nums[i] = t

        return nums

    def reverse(self, i, j, nums):
        idx = i
        while idx <= (i + j) / 2:
            nums = self.swap(idx, i + j - idx, nums)
            idx += 1

        return nums

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.nextPermutation([2,3,1])