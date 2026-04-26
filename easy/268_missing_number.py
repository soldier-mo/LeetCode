# description: https://leetcode.com/problems/missing-number/description/

class Solution(object):
    def missingNumber(self, nums):
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
            
def main():
    solver = Solution()  
    n = [0, 1]

    print(solver.missingNumber(n))

main()
 