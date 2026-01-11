


def binary_search(arr, target):
    size = len(arr)
    if size == 0:
        return -1
    
    l = 0
    r = size - 1

    if arr[l] >= target or arr[r] < target:
        if arr[l] == target:
            return l
        return -1
    
    while r - l > 1:
        mid = (l + r) // 2

        if arr[mid] < target:
            l = mid
        else:
            r = mid

    if arr[r] == target:
        return r
    
    return -1