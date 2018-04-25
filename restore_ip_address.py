import copy


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        acc = []
        self.backtracking(acc, s, [])
        ans = []

        for reversed_ip in acc:
            ans.append('.'.join(reversed_ip[::-1]))
        return ans

    def backtracking(self, acc, s, ip):
        if len(ip) > 4 or (len(ip) == 4 and len(s) > 0):
            return
        elif len(ip) == 4 and len(s) == 0:
            acc.append(copy.deepcopy(ip))
        else:
            for i in range(1, len(s) + 1):
                if int(s[-i:]) <= 255:
                    if s[-i:].startswith('0') and len(s[-i:]) > 1:
                        continue
                    else:
                        ip.append(s[-i:])
                        self.backtracking(acc, s[:-i], ip)
                        del ip[len(ip) - 1]
                else:
                    continue
            return
