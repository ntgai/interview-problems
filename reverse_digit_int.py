# Problem:
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''

class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        y = int(str(x)[::-1])

        if neg:
            y *= -1

        if not (-1*2**31 <= y < 2**31):
            return 0
        return y