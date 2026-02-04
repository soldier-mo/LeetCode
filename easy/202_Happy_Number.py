# description: https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        seenNumbers = set()

        while n != 1 and n not in seenNumbers:
            seenNumbers.add(n)
            n = sum(([int(x) ** 2 for x in str(n)]))

        return n == 1


def main():
    solver = Solution()
    n = 19
    n1 = 2

    print(solver.isHappy(n))
    print(solver.isHappy(n1))


main()
