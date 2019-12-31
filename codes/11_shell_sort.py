def shell_sort(alist):

    gap = len(alist) // 2

    while gap > 0:

        for i in range(gap, len(alist)):

            while i-gap >= 0 and alist[i] < alist[i-gap]:
                alist[i], alist[i-gap] = alist[i-gap], alist[i]
                i -= gap

        gap //= 2

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)