class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word = min(strs, key=len)
        while min_word: 
         if all([s.startswith(min_word) for s in strs]) : return min_word
         min_word = min_word[:-1]
        return min_word