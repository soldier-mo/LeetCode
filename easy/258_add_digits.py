# description: https://leetcode.com/problems/add-digits/description/


class Solution(object):
    def addDigits(self, num):
        while len(str(num)) > 1:
            num = self.sumDigits(num)
        return num

    def sumDigits(self, num):
        result = 0
        while num:
            result, num = result + num % 10, num // 10
        return result
    
    #
    # def addDigits(self, num):
    #     return 0 if num == 0 else 1 + (num - 1) % 9



def main():
    solver = Solution()
    input = 38

    print(solver.addDigits(input))


main()
