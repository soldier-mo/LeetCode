#description: https://leetcode.com/problems/remove-element/description/
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)

def main():
    nums = [0,1,3,0,4,2]
    val = 2
    solver = Solution()
    print(solver.removeElement(nums, val))
main()
