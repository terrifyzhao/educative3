def find_happy_number(num):
    slow, fast = num, num
    while 1:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))
        if slow == fast:
            break
    return slow == 1


def find_square_sum(num):
    sum = 0
    while num > 0:
        a = num % 10
        sum += a * a
        num = num // 10
    return sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
