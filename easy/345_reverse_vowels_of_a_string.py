# description: https://leetcode.com/problems/reverse-vowels-of-a-string/description/


class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        s_arr = list(s)

        left, right = 0, len(s_arr) - 1

        while left < right:
            while left < right and s_arr[left] not in vowels:
                left += 1

            while left < right and s_arr[right] not in vowels:
                right -= 1

            if left < right:
                s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
                left += 1
                right -= 1

        return "".join(s_arr)


def main():
    solver = Solution()
    s = "IceCreAm"

    print(solver.reverseVowels(s))


main()
