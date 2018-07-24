class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            c = list(word)
            c.sort()
            c = ''.join(c)
            if c in dic:
                dic[c].append(word)
            else:
                dic[c] = [word]

        r_list = []
        for k, v in dic.items():
            r_list.append(v)

        return r_list

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])