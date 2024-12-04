class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        '''
        Given - two strings
        if str2 can be a subseq of str1 by doing at most one operation

        case 1 : str2[j] == str1[i] # we match the char and move to next chars
        case 2 : str2[j]'s prev char is str1[i] # we can do the operation once on str1
        case 3 : move str1 index forward as we can't match
        If str2 is done - return True
        else - return False

        TC = O(min(len(str1), len(str2)) - just incrementing indices till one of the strings is done.
        SC = O(1) - used only indices
        '''
        if len(str1)<len(str2):
            return False
        i = 0 # index for str1
        j = 0 # index for str2
        while i<len(str1) and j<len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            elif (ord(str1[i])-ord('a')+1)%26 == (ord(str2[j])-ord('a'))%26:
                # we used the operation by shifting one char in str1.
                i += 1
                j += 1
            else:
                i += 1
        if j == len(str2):
            return True
        return False