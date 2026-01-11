def binarysearch(L, v):  #v = target element
    low = 0
    high = len(L) - 1
    while low <= high: 
        mid = (low + high) // 2
        if L[mid ] < v:
            low = mid  + 1
        elif L[mid ] > v:
            high = mid  - 1
        else:
            return mid
    return False