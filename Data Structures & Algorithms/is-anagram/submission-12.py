class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return True if (tuple(sorted(s)) == tuple(sorted(t))) else False
        #return ''.join(sorted(s)) == ''.join(sorted(t))
        if (set(s)!=set(t)) or (len(s)!=len(t)) : return False
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if s[i] in dict_s : dict_s[s[i]]+=1
            else: dict_s[s[i]]=1
            if t[i] in dict_t : dict_t[t[i]]+=1
            else: dict_t[t[i]]=1
        return dict_s.items()==dict_t.items()

