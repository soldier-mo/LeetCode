# description: https://leetcode.com/problems/power-of-three/description/


class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n //= 3
        return n == 1
        

def main():
    solver = Solution()
    n = 27

    print(solver.isPowerOfThree(n))


main()
