class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n%2 == 0:
            n = n//2
        return n==1
solution = Solution()
print(solution.isPowerOfTwo(16))  # Output: True

# solve the problem using recursion.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)

