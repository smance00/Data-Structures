def quick_sor(n, lo, hi):
    if lo < hi:
        k = partition(n, lo, hi)

        quick_sor(n, lo, k - 1)
        quick_sor(n, k + 1, hi)

def partition(n, lo, hi):
    pivot = n[hi]
    i = lo - 1

    for j in range(lo, hi):
        if n[j] < pivot:
            i += 1
            n[j], n[i] = n[i], n[j] # swap

    n[hi], n[i + 1] = n[i + 1], n[hi]  #swap

    return i + 1 #return from partition


def binary_algorithm(n, target):
    lo = 0
    hi = len(n)-1

    while lo <= hi:
        mid = (lo + hi) // 2

        if target == n[mid]:
            return mid

        if target < n[mid]:
            high = mid - 1

        else:
            lo = mid + 1
    return -1
