class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 0:
            return 0
        if len(ratings) == 1:
            return 1
        candy = [1] * len(ratings)
        sum = 0

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        sum += candy[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

            sum += candy[i]

        return sum


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.candy([1,3,2,2,1])