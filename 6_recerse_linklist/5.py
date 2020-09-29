from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head, rotations):
    cur = head
    length = 0
    while cur:
        length += 1
        cur = cur.next

    length = length - rotations % length

    pre = None
    cur = head
    i = 0
    while cur and i < length:
        i += 1
        pre = cur
        cur = cur.next
    pre.next = None

    tmp_head = cur

    while cur and cur.next:
        cur = cur.next

    cur.next = head

    return tmp_head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
