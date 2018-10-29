class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        dic = {}
        for e in emails:
            _at = False
            _plus = False
            _address = ''
            for c in e:
                if _at:
                    _address += c
                else:
                    if c == '+':
                        _plus = True
                        continue
                    if c == '@':
                        _at = True
                        _address += c
                        continue
                    if c == '.':
                        continue
                    if _plus:
                        continue
                    else:
                        _address += c
            if dic.has_key(_address):
                dic[_address] += 1
            else:
                dic[_address] = 1

        return len(dic.keys())




if __name__ == '__main__':
    # begin
    s = Solution()

    print s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])