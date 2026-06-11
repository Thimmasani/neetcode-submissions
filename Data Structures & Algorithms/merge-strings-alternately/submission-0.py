class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        min_len = min(word1_len,word2_len)
        merged_string = ""
        for i in range(min_len):
            merged_string += word1[i]+word2[i]
        return merged_string+word1[min_len:]+word2[min_len:]