# description: https://leetcode.com/problems/reverse-integer/description/


class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        reversed_x = int(str(abs(x))[::-1]) * sign

        return reversed_x if -2_147_483_648 <= reversed_x <= 2_147_483_647 else 0


def main():
    solution = Solution()
    x = -123

    print(solution.reverse(x))


main()
