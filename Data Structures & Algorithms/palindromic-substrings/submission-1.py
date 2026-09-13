class Solution:
    def countSubstrings(self, s: str) -> int:
        def no_of_palindromes_at_index(i):
            if i== len(s)-1 : return 1
            else:
                count=1
                start = i-1
                move = 1
                while (i+move)< len(s):
                    if s[i]==s[i+move]:
                        count+=1
                        move+=1
                    else:
                        break
                end = i+move

                while (start>=0) and end<len(s):
                    if s[start]==s[end] : 
                        count+=1
                        start-=1
                        end+=1
                    else : return count

                return count

        result = 0
        for i in range(len(s)):
            result += no_of_palindromes_at_index(i)
        
        return result