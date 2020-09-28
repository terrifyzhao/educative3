from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    slow, fast = head, head
    pre = None
    while fast and fast.next:
        pre = slow
        slow = slow.next

        fast = fast.next.next
    pre.next = None
    tail = reverse(slow)
    cur = head

    while cur and tail:
        head_tmp = cur.next
        cur.next = tail
        cur = head_tmp

        tail_tmp = tail.next
        tail.next = cur
        tail = tail_tmp

    return head


def reverse(head):
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()
