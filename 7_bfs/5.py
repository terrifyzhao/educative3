from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    queue = deque()
    queue.append(root)

    length = 0
    while queue:
        size = len(queue)
        length += 1
        for _ in range(size):
            node = queue.popleft()
            if node.left is None and node.right is None:
                return length
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return 0


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
