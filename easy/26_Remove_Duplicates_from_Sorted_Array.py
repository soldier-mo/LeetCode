#description: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] in nums[:i] and nums[i] != "_":
                nums.pop(i)
                nums.append("_")
            else:
                i+=1
        return sum(1 for x in nums if isinstance(x, (int, float)))

def main():
    nums = [1,1,2]
    solver = Solution()
    print(solver.removeDuplicates(nums))
main()