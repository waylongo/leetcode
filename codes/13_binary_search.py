def binary_search(alist, item):

    if len(alist) <= 1:
        return

    mid_idx = len(alist) // 2

    if alist[mid_idx] == item:
        return True
    elif alist[mid_idx] < item:
        binary_search(alist[mid_idx:], item)
    else:
        binary_search(alist[:mid_idx], item)

    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))