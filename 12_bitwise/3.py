def calculate_bitwise_complement(n):
    length = 0
    tmp = n
    while n:
        n = n >> 1
        length += 1

    num = pow(2, length) - 1

    return num ^ tmp


def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()
