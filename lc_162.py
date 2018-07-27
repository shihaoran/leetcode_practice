class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.n = nums
        return self.find(0, len(nums) - 1)

    def find(self, low, high):
        if low == high: return low
        mid1 = (low + high) / 2
        mid2 = mid1 + 1
        if self.n[mid1] > self.n[mid2]:
            return self.find(low, mid1)
        else:
            return self.find(mid2, high)

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.findPeakElement([1,2,3,1])