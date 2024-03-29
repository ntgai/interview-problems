# Problem:
'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
'''

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        dec_cnt = 0

        ran = range(0, len(nums))
        for i in ran:
            if i+1 in ran:
                if nums[i]>nums[i+1]:
                    dec_cnt += 1
                    if i-1 in ran:
                        if nums[i-1]>nums[i+1]:
                            if i+2 in ran:
                                if nums[i]>nums[i+2]:
                                    return False
            if(dec_cnt) > 1:
                return False
        return True