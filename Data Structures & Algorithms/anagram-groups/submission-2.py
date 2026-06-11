from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in hashmap : hashmap[key] = [word] 
            else : hashmap[key].append(word)
        return list(hashmap.values())
