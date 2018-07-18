class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.containsNearbyDuplicate([1,2,3,1,2,3], 2)