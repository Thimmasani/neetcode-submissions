import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left=0
        right = len(filtered_text)-1
        while left<right:
            if filtered_text[left] == filtered_text[right]: 
                left += 1; right -=1
            else :
                return False
        return True
