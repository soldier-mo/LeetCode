# description: https://leetcode.com/problems/symmetric-tree/description/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, r, l):
        if not r and not l:
            return True
        if not r or not l or r.val != l.val:
            return False
        return self.isMirror(r.left, l.right) and self.isMirror(r.right, l.left)


#####################################
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
    p = create_tree_from_list([1, 2, 2, 3, 4, 4, 3])
    q = create_tree_from_list([1, 2, 2, None, 3, None, 3])
    solver = Solution()
    # print(solver.isSymmetric(q))
    print(solver.isSymmetric(p))


main()
