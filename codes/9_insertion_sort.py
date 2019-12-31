def insertion_sort(alist):
    """insertion sort"""
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j-1], alist[j] = alist[j], alist[j-1]


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(li)
print(li)
