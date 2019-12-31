def binary_search_recursive(alist, item):
    if len(alist) == 0:
        return False

    mid_idx = len(alist) // 2

    if alist[mid_idx] == item:
        return True
    elif alist[mid_idx] < item:
        return binary_search_recursive(alist[mid_idx + 1:], item)
    else:
        return binary_search_recursive(alist[:mid_idx], item)


def binary_search(alist, item):
    low, high = 0, len(alist) - 1

    while low < high:
        mid_idx = (low + high) // 2
        if alist[mid_idx] == item:
            return True
        elif alist[mid_idx] < item:
            low = mid_idx + 1
        else:
            high = mid_idx - 1

    return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search_recursive(testlist, 3))
print(binary_search_recursive(testlist, 13))

print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
