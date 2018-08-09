class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s, e = 0, len(nums) - 1
        while s < e:
            m = s + (e-s)/2
            if nums[m-1] < nums [m] < nums[m+1]:
                return nums[m]
            elif nums[m-1] < nums[m]:
                if (e-m+1) % 2 == 0:
                    e = m - 1
                else:
                    s = m
            else:
                if (m-s+1) % 2 == 0:
                    s = m + 1
                else:
                    e = m
        return nums[s]


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])