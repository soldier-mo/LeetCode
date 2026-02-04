# description: https://leetcode.com/problems/path-sum/description/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # if a leaf and the target sum is reached return True
        if not root.right and not root.left and targetSum - root.val == 0:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )


#####################################0
#               Helper              #
#####################################


def create_tree_from_list(lst):
    if not lst:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


###################################
#               main              #
###################################


def main():
    root1 = create_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    targetSum1 = 22
    root2 = create_tree_from_list([1, 2, 3])
    targetSum2 = 5
    solver = Solution()
    print(solver.hasPathSum(root1, targetSum1))
    print(solver.hasPathSum(root2, targetSum2))


main()
