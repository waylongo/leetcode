def quick_sort(alist, low, high):

    if low >= high:
        return

    pivot = alist[low]

    while low < high:
        while low < high and alist[high] > pivot:
            high -= 1

        alist[low] = alist[high]

        while low < high and alist[low] <= pivot:
            low += 1

        alist[high] = alist[low]

    alist[low] = pivot

    quick_sort(alist, 0, low-1)
    quick_sort(alist, low+1, high)

li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(li, 0, len(li)-1)
print(li)
