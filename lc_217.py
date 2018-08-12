class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for n in nums:
            if dic.has_key(n):
                return True
            else:
                dic[n] = True
        return False


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.containsDuplicate([1,2,3,4])