# description: https://leetcode.com/problems/power-of-two/description/

import math


class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0


def main():
    solver = Solution()

    print(solver.isPowerOfTwo(8))
    print(solver.isPowerOfTwo(16))
    print(solver.isPowerOfTwo(3))

main()
