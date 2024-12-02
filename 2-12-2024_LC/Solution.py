class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        '''
        Given - sentence with words, searchWord
        check if searchWord is the prefix of any word
        Return Min index or -1

        Idea 1 - Go to every word and check if searchWord is the prefix or not.
                TC = O(W*M) - w words and m is len of searchword
                SC = O(N) - for words
        Idea 2 - As we go from word to word we store in the sentence we can check for the searchWOrd with out any storing of words.
                TC = O(N) - going through the sentence of len n
                SC = O(1) - only storing indices and a boolean value
        '''
        # words = sentence.split()
        # m = len(searchWord)
        # for ind, word in enumerate(words):
        #     if len(word) >= m:
        #         is_word = True
        #         i = 0
        #         while i<m:
        #             if searchWord[i] != word[i]:
        #                 is_word = False
        #                 break
        #             i += 1
        #         if is_word:
        #             return ind+1    # 1-indexed sentence
        # return -1

        word = 1
        i = j = 0
        m = len(searchWord)
        n = len(sentence)
        is_word = True
        while i<n:
            if sentence[i] == " ":
                # start of a new word
                j = 0
                word += 1
                is_word = True
                i += 1
            while j<m and i<n and sentence[i]!= " ":
                if sentence[i] != searchWord[j]:
                    is_word = False
                    break
                i += 1
                j += 1
            if not is_word:
                while i<n and sentence[i]!= " ":
                    i += 1
            elif j==m: return word
        return -1