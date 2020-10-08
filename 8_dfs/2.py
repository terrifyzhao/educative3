class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    find(root, sum, [], allPaths)
    return allPaths


def find(root, sum, cur, all):
    if not root:
        return 0

    cur.append(root.val)

    if root.val == sum and root.left is None and root.right is None:
        all.append(list(cur))
    else:
        find(root.left, sum - root.val, cur, all)
        find(root.right, sum - root.val, cur, all)

    cur.remove(root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
