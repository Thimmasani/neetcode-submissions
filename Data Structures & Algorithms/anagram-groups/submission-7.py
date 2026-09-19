class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        for s in strs:
            temp = tuple(sorted(s))
            if temp in hash_map: hash_map[temp].append(s)
            else : hash_map[temp] = [s]
        
        return list(hash_map.values())