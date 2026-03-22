# description: https://leetcode.com/problems/binary-tree-paths/description/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []

        result = []

        def dfs(node, path):
            if not node:
                return


            path += str(node.val)

            # leaf found
            if not node.left and not node.right:
                result.append(path)
                return


            dfs(node.left, path + "->")
            dfs(node.right, path + "->")

        dfs(root, "")
        return result


def main():
    #       2
    #      / \
    #     1   3

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.left.left = TreeNode(6)

    solution = Solution()

    print(solution.binaryTreePaths(root))


main()
