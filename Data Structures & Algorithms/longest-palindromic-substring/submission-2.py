class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest_palindrome_at_an_index(i):
            if len(s)==1 : return s
            elif i==len(s)-1 : return s[i]
            else:
                start=i-1
                count=1
                while (i+count)<len(s) :
                    if s[i]==s[i+count]:
                        count+=1
                    else:
                        break
                end = i+count
                temp_palindrome = s[i:i+count]
                while (start>=0) and (end<len(s)):
                    if s[start]==s[end]:
                        temp_palindrome = s[start:end+1]
                        start-=1
                        end+=1
                    else: return temp_palindrome
                return temp_palindrome

        result = ""
        for i in range(len(s)):
            index_palindrome = longest_palindrome_at_an_index(i)
            result = result if len(result)>len(index_palindrome) else index_palindrome
        return result