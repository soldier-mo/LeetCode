class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i,j]


def main():
    nums = [2,7,11,15]
    target = 9
    solver = Solution()
    print(solver.twoSum(nums, target))
main()
