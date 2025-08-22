class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        return str(x) == str(x)[::-1]

"""
Time Complexity: O(n)
- Converting the integer to a string takes O(n), where n is the number of digits.
- Reversing the string also takes O(n).
- Comparison of both strings again takes O(n).
So overall: O(n).

Space Complexity: O(n)
- The string representation of the number takes O(n) extra space.
- Reversing creates another O(n) copy.
So overall: O(n).
"""
