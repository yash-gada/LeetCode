# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        s = s.lower()
      
        new = "".join([i for i in s if(i.isalnum() == True)])

        return new==new[::-1]


# Alternate Solution
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        s = s.lower()
        
        for i in s:
            if (96 < ord(i) < 123) or (46 < ord(i) < 58):
                new += i

        return new==new[::-1]
'''
