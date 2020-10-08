class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    return cal_sum(root, 0)


def cal_sum(node, cur_sum):
    if not node:
        return 0
    cur_sum = cur_sum * 10 + node.val
    if node.left is None and node.right is None:
        return cur_sum
    return cal_sum(node.left, cur_sum) + cal_sum(node.right, cur_sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
