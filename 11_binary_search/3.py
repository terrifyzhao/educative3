def search_next_letter(letters, key):
    start, end = 0, len(letters) - 1

    if key > letters[-1]:
        return letters[0]

    while start <= end:
        mid = start + (end - start) // 2

        if letters[mid] == key:
            return letters[mid + 1]
        elif letters[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return letters[start]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
