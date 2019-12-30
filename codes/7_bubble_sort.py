def bubble_sort(alist):
    """bubble sort"""
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(li)
print(li)

# O(n^2)