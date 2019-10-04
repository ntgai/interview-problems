# valid palindrome?

class Solution:
    def isPalindrome(self, s: str) -> bool:
    	# checking if char is alphanumeric and merging them into new str
        st = ''.join(l for l in s.lower() if l.isalnum())
        # alternatively we can use s.casefold() instead s.lower()

        # list[::-1] -> make reverse
        return st == st[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen = ''.join(l for l in s.lower() if l.isalnum())
        for i in range(0, int(len(sen)/2)):
            if sen[i] != sen[len(sen)-i-1]:
                return False
        return True


