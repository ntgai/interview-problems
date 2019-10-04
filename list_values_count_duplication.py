# Problem:
'''Given an array of integers arr, write a function that returns true if and 
	only if the number of occurrences of each value in the array is unique'''

'''
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
        
        # converting list to set, because set contains only unique values then check len with origin list
        s = set(d.values())
        if(len(d.values()) == len(s)):
            return True
        else:
            return False

#alternative solution using Counter
from collections import Counter
class Solution(object):
	def uniqueOccurrences(self, arr):
		ctr = Counter(arr)
		return len(set(ctr.values()))==len(ctr.values())