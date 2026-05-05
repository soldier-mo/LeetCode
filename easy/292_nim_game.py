# description: https://leetcode.com/problems/nim-game/description/


class Solution(object):
    def canWinNim(self, n):
        return n % 4 != 0


def main():
    solver = Solution()
    n = 8

    print(solver.canWinNim(n))


main()
