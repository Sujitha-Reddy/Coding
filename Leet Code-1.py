Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Example 1:
Input: 121 Output: true 
Example 2:
Input: -121 Output: false 
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome. 
Example 3:
Input: 10 Output: false 
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


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
