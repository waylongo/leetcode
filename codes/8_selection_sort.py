def selection_sort(alist):
    """selection sort"""

    for i in range(len(alist)):
        min_idx = i
        for j in range(i+1, len(alist)):
            if alist[j] < alist[min_idx]:
                min_idx = j
        alist[min_idx], alist[i] = alist[i], alist[min_idx]

li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(li)
print(li)