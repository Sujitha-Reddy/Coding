#1. Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Example 1:
# Input: 121 Output: true 
# Example 2:
# Input: -121 Output: false 
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome. 
# Example 3:
# Input: 10 Output: false 
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        num=x
        while x > 0:
            dig=x%10
            rev=rev*10+dig
            x=x//10   
        if(num==rev):
            return True
        else:
            return False
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]]=i
            else:
                return [dict[target-nums[i]],i]
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:  [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x= int(str(x)[::-1])
        if x<=0:
            x=-1*int(str(x*-1)[::-1])
        return x if x<=(2**31-1) and x>=-(2**31) else 0
 
