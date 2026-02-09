# description: https://leetcode.com/problems/summary-ranges/description/


class Solution(object):
    def summaryRanges(self, nums):
        result = []
        start = nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i-1]))
            
                if i < len(nums):
                    start = nums[i]

        return result


def main():
    solver = Solution()

    print(solver.summaryRanges([0, 1000000]))
    print(solver.summaryRanges([0, 1, 2, 4, 5, 7]))


main()
