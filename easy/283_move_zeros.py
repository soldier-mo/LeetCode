# description: https://leetcode.com/problems/move-zeroes/description/

class Solution(object):
    def moveZeroes(self, nums):
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        return nums


def main():
    solver = Solution()
    n = [1, 0, 2, 3]

    print()
    print(solver.moveZeroes(n))


main()

# pos = 0         -> pos = 1
# [(1), 0, 2, 3]

# pos = 1
# [1, (0), 2, 3]

# pos = 1         ->  pos = 2
# [1, 0, (2), 3]  ->  [1, 2, 0, 3]

# pos = 2         -> pos = 3
# [1, 2, 0, (3)]  -> [1, 2, 3, (0)]

# return [1, 2, 3, 0]
