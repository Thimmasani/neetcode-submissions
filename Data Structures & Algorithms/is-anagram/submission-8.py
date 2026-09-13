class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if (tuple(sorted(s)) == tuple(sorted(t))) else False
        return ''.join(sorted(s)) == ''.join(sorted(t))
        #if (set(s)!=set(t)) or (len(s)==len(t)) : return False
        #dict_s = dict_t = {}

