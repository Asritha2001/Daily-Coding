from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        '''
        Given - string 's' and array spaces
        add before the char at index in spaces array
        Idea 1 : Go through the string and keep track of index we are at and add to the res string.
                TC = O(N+M), n=len(s)
                SC = O(1), not considering the output string

        Idea 2 : slice the string and add to the list and return the res string.
                TC = O(N+M), n=len(s), m = len(spaces)
                SC = O(M), fot the list
        '''
        # res = ""
        # j = 0
        # for i,ch in enumerate(s):
        #     if j<len(spaces) and i == spaces[j]:
        #         res += " "
        #         j += 1
        #     res += s[i]
        # return res

        i = 0
        res = []
        for space in spaces:
            res.append(s[i:space])
            i = space
        res.append(s[i:])
        return " ".join(res)