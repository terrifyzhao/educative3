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


def reverse_sub_list(head, p, q):
    first_part_tail = None
    second_part_head = None

    position = 1
    pre = None
    cur = head
    while cur:
        if position == p:
            first_part_tail = pre
            second_part_head = cur
            break
        position += 1
        pre = cur
        cur = cur.next

    pre = None
    while cur and position <= q:
        position += 1
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    if first_part_tail is not None:
        first_part_tail.next = pre
    else:
        head = pre
    second_part_head.next = cur

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
