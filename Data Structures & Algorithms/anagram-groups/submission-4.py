from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            # Count of each of the 26 lowercase letters -> tuple as key.
            # tuple is hashable so it can be a dict key.
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())
