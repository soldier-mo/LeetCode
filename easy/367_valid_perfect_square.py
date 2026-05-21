# description: https://leetcode.com/problems/valid-perfect-square/description/


class Solution(object):
    def isPerfectSquare(self, num):
        odd = 1
        while num > 0:
            num -= odd
            odd +=2
        
        return num == 0



def main():
    solver = Solution()
    num = 9

    print(solver.isPerfectSquare(num))


main()
