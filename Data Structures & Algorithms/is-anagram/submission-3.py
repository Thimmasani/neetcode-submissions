class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if (tuple(sorted(s)) == tuple(sorted(t))) else False