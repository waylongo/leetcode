def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    mid_idx = len(alist) // 2
    left_li = merge_sort(alist[:mid_idx])
    right_li = merge_sort(alist[mid_idx:])

    return merge(left_li, right_li)


def merge(left, right):
    alist = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            alist.append(left[l])
            l += 1
        else:
            alist.append(right[r])
            r += 1
    alist += left[l:]
    alist += right[r:]

    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_alist = merge_sort(alist)
print(sorted_alist)
