#description: https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)
        
def main():
    nums = [1,3,5,6]
    target = 7
    solver = Solution()
    print(solver.searchInsert(nums, target))
main()
