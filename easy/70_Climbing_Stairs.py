#description: https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        one_step_behind_ways = 3
        two_step_behind_ways = 2
        current_step_ways = 5 # step 4 have 5 distinct ways

        current_step = 4

        while current_step < n:
            two_step_behind_ways = one_step_behind_ways
            one_step_behind_ways = current_step_ways
            current_step_ways = one_step_behind_ways + two_step_behind_ways
            
            current_step += 1

        return current_step_ways

def main():
    solver = Solution()
    n = 5
    print(solver.climbStairs(n))
main()