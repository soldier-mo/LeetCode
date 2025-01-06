#description: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen: 
                return [seen[diff], i]
            seen[num] = i  


def main():
    nums = [2,7,11,15]
    target = 9
    solver = Solution()
    print(solver.twoSum(nums, target))
main()
