def remove_element(arr, key):
    next = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[next] = arr[i]
            next += 1
    return next

def main():
    print("Array new length: " +
          str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " +
          str(remove_element([2, 11, 2, 2, 1], 2)))


main()
