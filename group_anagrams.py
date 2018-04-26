class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = {}
        for word in strs:
            sorted_str = ''.join(sorted(word))
            if sorted_str in dict:
                dict[sorted_str].append(word)
            else:
                dict[sorted_str] = [word]


        return [value for _, value in dict.items()]