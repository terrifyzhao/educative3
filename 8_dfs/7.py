import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumPathSum:

    def find_maximum_path_sum(self, root):
        self.globalMaximumSum = -math.inf
        self.find_maximum_path_sum_recursive(root)
        return self.globalMaximumSum

    def find_maximum_path_sum_recursive(self, root):
        if not root:
            return 0
        left = self.find_maximum_path_sum_recursive(root.left)
        right = self.find_maximum_path_sum_recursive(root.right)

        left = max(left, 0)
        right = max(right, 0)

        tmp_sum = left + root.val + right
        self.globalMaximumSum = max(self.globalMaximumSum, tmp_sum)

        return max(left, right) + root.val


def main():
    maximumPathSum = MaximumPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()
