# Problem: Power of Three
# Determine whether a given integer n is a power of three.

"""
Approach 🚀

1. Handle base cases:
   - If n <= 0, return False because negative numbers and zero cannot be powers of 3.
   - If n == 1, return True because 3^0 = 1.
   - If n == 3, return True because 3^1 = 3.

2. For other cases:
   - Keep dividing n by 3 as long as it is divisible by 3 (n % 3 == 0).
   - After the loop ends, check if the result is equal to 1.
     If yes → n is a power of 3.
     If no  → n is not a power of 3.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        if n <= 0:
            return False

        if n == 3:
            return True

        while n % 3 == 0:
            n //= 3

        return n == 1


"""
Time Complexity: O(log₃ n) → because we keep dividing n by 3.
Space Complexity: O(1) → only constant extra space is used.
"""
