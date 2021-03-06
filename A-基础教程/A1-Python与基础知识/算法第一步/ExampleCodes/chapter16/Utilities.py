import random


def swap(arr, i, j):
    if len(arr) < 2:
        return

    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr):
        return

    if i == j:
        return

    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

    return


def partition(arr, low, high):
    if low >= high:
        return -1

    left_partition = []
    right_partition = []
    pivot = arr[low]

    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            left_partition.append(arr[i])
        else:
            right_partition.append(arr[i])

    llen = len(left_partition)
    rlen = len(right_partition)

    for i in range(0, llen):
        arr[i + low] = left_partition[i]
        arr[low + llen] = pivot

    for i in range(0, rlen):
        arr[i + low + llen + 1] = right_partition[i]

    return low + llen


def partition_v2(arr, low, high):
    if low >= high:
        return -1

    pi = low
    li = low + 1
    ri = high

    while ri >= li:
        if arr[li] > arr[pi]:
            swap(arr, ri, li)
            ri -= 1
        else:
            li += 1

    pi = li - 1
    swap(arr, low, pi)
    return pi


def generate_test_data(start, end, len=None):
    arr_random = None

    if len is not None:
        arr_random = [random.randint(start, end) for x in range(0, len)]
    arr_seq = [x for x in range(start, end + 1)]
    arr_reverse = [end + 1 - x for x in range(start, end + 1)]

    return arr_random, arr_seq, arr_reverse

def qsort_recursion(arr, low, high):
    if low >= high:
        return

    p = partition_v2(arr, low, high) #调用新的分区函数
    qsort_recursion(arr, low, p - 1)
    qsort_recursion(arr, p + 1, high)

    return